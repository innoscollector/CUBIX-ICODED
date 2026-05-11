"""
CUBIX-ICODED — Full Physics Simulation
=======================================
Generates:
1. Icosahedral + Dodecahedral geometry (CAD data as JSON)
2. Magnetic flux density field (Halbach array simulation)
3. Torque vs RPM curve
4. Back-EMF per harvesting gate
5. Concentric layer stress analysis
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.colors import Normalize
import matplotlib.cm as cm
import json, os

OUT = "/mnt/user-data/outputs/"
os.makedirs(OUT, exist_ok=True)

PHI = (1 + np.sqrt(5)) / 2
EDGE_MM = 115.34
BEVEL_DEG = 20.905
OFFSET_DEG = 31.71
NUM_MAGNETS = 60
NUM_CLUSTERS = 12
MAGNET_BR = 1.05          # SmCo N52 remanence (Tesla)
MAGNET_VOL = 25e-3*10e-3*5e-3  # m³ per magnet
MU0 = 4*np.pi*1e-7
AIR_GAP = 0.30e-3         # 0.30 mm
ROTOR_R = 90e-3           # 90 mm
STATOR_R = 118e-3         # 118 mm

# ─── GEOMETRY ────────────────────────────────────────────────────

def icosahedron_vertices(scale=1.0):
    verts = []
    for s in [1,-1]:
        for t in [1,-1]:
            verts.append([0, s, t*PHI])
            verts.append([s, t*PHI, 0])
            verts.append([t*PHI, 0, s])
    verts = np.array(verts, dtype=float)
    edge = np.linalg.norm(verts[0]-verts[1])
    return verts / edge * scale

def icosahedron_faces(verts):
    n = len(verts)
    edge = np.linalg.norm(verts[0]-verts[1])
    tol = edge*0.01
    faces = []
    for i in range(n):
        for j in range(i+1,n):
            if abs(np.linalg.norm(verts[i]-verts[j])-edge)<tol:
                for k in range(j+1,n):
                    if (abs(np.linalg.norm(verts[i]-verts[k])-edge)<tol and
                        abs(np.linalg.norm(verts[j]-verts[k])-edge)<tol):
                        faces.append([i,j,k])
    return faces

def dodecahedron_vertices(scale=1.0):
    verts = []
    for a in [1,-1]:
        for b in [1,-1]:
            for c in [1,-1]:
                verts.append([a,b,c])
    for s in [1,-1]:
        for t in [1,-1]:
            verts.append([0, s/PHI, t*PHI])
            verts.append([s/PHI, t*PHI, 0])
            verts.append([t*PHI, 0, s/PHI])
    verts = np.array(verts, dtype=float)
    edge = min(np.linalg.norm(verts[i]-verts[j])
               for i in range(len(verts)) for j in range(i+1,len(verts)))
    return verts / edge * scale

# ─── MAGNETIC FIELD SIMULATION ───────────────────────────────────

def halbach_field_1d(theta_array, n_poles=12, Br=MAGNET_BR, r=ROTOR_R):
    """
    Simplified 1D Halbach field along stator circumference.
    4:1 asymmetry: strong side inward, weak side outward.
    Returns B_radial (T) at each theta.
    """
    B = np.zeros_like(theta_array)
    for k in range(1, 5):  # 4 harmonics for Halbach
        amplitude = Br * (1/(k)) * np.exp(-k * AIR_GAP / r)
        B += amplitude * np.cos(k * n_poles/2 * theta_array)
    # 4:1 Halbach asymmetry boost on inward face
    B_inner = B * 4.0
    B_outer = B * 1.0
    return B_inner, B_outer

def compute_flux_grid():
    """2D flux density map in rotor-stator gap cross-section."""
    theta = np.linspace(0, 2*np.pi, 360)
    r_vals = np.linspace(ROTOR_R, STATOR_R, 50)
    TH, RR = np.meshgrid(theta, r_vals)
    
    B = np.zeros_like(TH)
    for cluster_i in range(12):
        cluster_angle = 2*np.pi * cluster_i / 12
        for mag_j in range(5):
            mag_angle = cluster_angle + 2*np.pi*mag_j/5 * 0.4
            d_theta = TH - mag_angle
            dist = np.sqrt(RR**2 + ROTOR_R**2 - 2*RR*ROTOR_R*np.cos(d_theta))
            dist = np.maximum(dist, 1e-4)
            B += MAGNET_BR * (MAGNET_VOL / (4*np.pi)) / dist**2
    
    return TH, RR, B

# ─── TORQUE & EMF SIMULATION ─────────────────────────────────────

def torque_vs_rpm():
    """Electromagnetic torque curve accounting for Back-EMF."""
    rpm_range = np.linspace(0, 30000, 500)
    omega = rpm_range * 2*np.pi / 60
    
    # Coil parameters
    N_turns_harvest = 120
    N_turns_impulse = 80
    R_coil = 2.5          # Ohm per harvesting coil
    L_coil = 1.2e-3       # Henry
    
    # Back-EMF per coil: e = N * dΦ/dt = N * B * A * omega
    A_coil = np.pi * (17.5e-3)**2  # coil area ~35mm diameter
    B_avg = 0.42                    # average flux density at stator (T)
    
    # 9 harvesting coils
    EMF_harvest = 9 * N_turns_harvest * B_avg * A_coil * omega
    EMF_impulse = 3 * N_turns_impulse * B_avg * A_coil * omega
    
    # Current limited by impedance Z = sqrt(R² + (ωL)²)
    Z_harvest = np.sqrt(R_coil**2 + (omega * L_coil)**2)
    I_harvest = EMF_harvest / (9 * Z_harvest)
    
    # Torque = F * r = B * I * l * N * r (9 coils)
    l_coil = 2 * np.pi * 17.5e-3  # effective conductor length per turn
    T_electromagnetic = 9 * N_turns_harvest * B_avg * I_harvest * l_coil * ROTOR_R
    
    # Mechanical losses (bearing friction + windage)
    T_friction = 0.015 + 1.8e-8 * omega**1.8
    
    T_net = T_electromagnetic - T_friction
    P_output = T_net * omega
    
    # Efficiency
    P_input = T_electromagnetic * omega
    efficiency = np.where(P_input > 0.01, np.clip(P_output/P_input, 0, 1), 0)
    
    return rpm_range, T_net, T_friction, T_electromagnetic, EMF_harvest, efficiency

def gate_emf_phase():
    """EMF waveforms for 3 impulse + 9 harvesting gates at 3000 RPM."""
    t = np.linspace(0, 0.02, 1000)  # 20ms window
    omega = 3000 * 2*np.pi / 60
    
    N_h = 120; N_i = 80
    B = 0.42; A = np.pi*(17.5e-3)**2
    
    # Impulse gates (0°, 120°, 240°)
    impulse = {}
    for i, ang in enumerate([0, 120, 240]):
        phase = np.radians(ang)
        impulse[f'I{i+1}'] = N_i * B * A * omega * np.sin(omega*t + phase)
    
    # Harvesting triplets with 31.71° offset
    harvest = {}
    idx = 1
    for base in [0, 120, 240]:
        for delta in [OFFSET_DEG, OFFSET_DEG*2, OFFSET_DEG*3]:
            phase = np.radians(base + delta)
            harvest[f'H{idx}'] = N_h * B * A * omega * np.sin(omega*t + phase)
            idx += 1
    
    return t, impulse, harvest

# ─── STRESS / STRUCTURAL ─────────────────────────────────────────

def rotor_stress_vs_rpm():
    """Hoop stress in PEEK-CF rotor panel at different RPMs."""
    rpm = np.linspace(0, 30000, 400)
    omega = rpm * 2*np.pi / 60
    
    rho_peek_cf = 1420   # kg/m³
    E_peek_cf = 12e9     # Pa (Young's modulus)
    nu = 0.38            # Poisson's ratio
    r_mean = ROTOR_R
    
    # Rotating disk hoop stress: σ_hoop = ρ·ω²·r²·(3+ν)/4
    sigma_hoop = rho_peek_cf * omega**2 * r_mean**2 * (3+nu)/4
    
    # Centrifugal force on each SmCo magnet (25×10×5mm, ρ=8400 kg/m³)
    m_magnet = 25e-3 * 10e-3 * 5e-3 * 8400
    F_centrifugal = m_magnet * omega**2 * r_mean  # per magnet
    
    # PEEK-CF tensile strength: ~180 MPa; safety factor
    sigma_yield = 180e6
    safety_factor = sigma_yield / np.maximum(sigma_hoop, 1e3)
    
    return rpm, sigma_hoop/1e6, F_centrifugal, safety_factor

# ─── PLOTTING ────────────────────────────────────────────────────

DARK = '#0a0e1a'
BLUE = '#00aaff'
ORANGE = '#ff6600'
GREEN = '#00ff99'
PURPLE = '#aa88ff'
YELLOW = '#ffdd00'
RED = '#ff4444'

def style_ax(ax, title='', xlabel='', ylabel=''):
    ax.set_facecolor('#0d1117')
    ax.tick_params(colors='#888888', labelsize=8)
    ax.spines['bottom'].set_color('#333333')
    ax.spines['top'].set_color('#333333')
    ax.spines['left'].set_color('#333333')
    ax.spines['right'].set_color('#333333')
    if title: ax.set_title(title, color='white', fontsize=10, pad=8)
    if xlabel: ax.set_xlabel(xlabel, color='#888888', fontsize=8)
    if ylabel: ax.set_ylabel(ylabel, color='#888888', fontsize=8)
    ax.grid(color='#1a2233', linewidth=0.5, linestyle='--')

# ── FIG 1: 3D CAD ──

def fig_cad_3d():
    scale = EDGE_MM / 2
    ico_v = icosahedron_vertices(scale)
    ico_f = icosahedron_faces(ico_v)
    
    dod_scale = scale * 1.30
    dod_v = dodecahedron_vertices(dod_scale)
    
    fig = plt.figure(figsize=(14, 11))
    fig.patch.set_facecolor(DARK)
    
    # Main 3D CAD view
    ax = fig.add_subplot(2,2,(1,3), projection='3d')
    ax.set_facecolor('#0a0e1a')
    
    # Dodecahedral stator (outer)
    ax.scatter(dod_v[:,0], dod_v[:,1], dod_v[:,2],
               color=GREEN, s=30, alpha=0.5, zorder=2)
    for i in range(len(dod_v)):
        for j in range(i+1, len(dod_v)):
            d = np.linalg.norm(dod_v[i]-dod_v[j])
            edge_len = min(np.linalg.norm(dod_v[a]-dod_v[b])
                          for a in range(len(dod_v)) for b in range(a+1,len(dod_v)))
            if abs(d - edge_len) < edge_len*0.05:
                xs = [dod_v[i,0], dod_v[j,0]]
                ys = [dod_v[i,1], dod_v[j,1]]
                zs = [dod_v[i,2], dod_v[j,2]]
                ax.plot(xs,ys,zs, color=GREEN, alpha=0.25, lw=0.7)
    
    # Icosahedral rotor (inner)
    polys = [[ico_v[i] for i in f] for f in ico_f]
    coll = Poly3DCollection(polys, alpha=0.18, linewidths=0.8,
                            edgecolors=BLUE, facecolors='#0d2a4a')
    ax.add_collection3d(coll)
    
    # Magnet clusters at vertices
    ax.scatter(ico_v[:,0], ico_v[:,1], ico_v[:,2],
               color=RED, s=90, zorder=6, label='SmCo cluster (×12)')
    
    # Halbach arrows
    for v in ico_v:
        rad = v / np.linalg.norm(v)
        perp = np.cross(rad, [0,0,1])
        if np.linalg.norm(perp)<0.01: perp = np.cross(rad,[0,1,0])
        perp /= np.linalg.norm(perp)
        for k in range(5):
            angle = 2*np.pi*k/5
            rot = perp*np.cos(angle) + np.cross(rad,perp)*np.sin(angle)
            al = scale*0.22
            ax.quiver(v[0],v[1],v[2],
                      rot[0]*al,rot[1]*al,rot[2]*al,
                      color=YELLOW, alpha=0.65, lw=0.7, arrow_length_ratio=0.3)
    
    # Stator gate markers
    impulse_idx = [0, 4, 8]
    harvest_idx = [i for i in range(20) if i not in impulse_idx]
    ax.scatter(dod_v[impulse_idx,0], dod_v[impulse_idx,1], dod_v[impulse_idx,2],
               color=ORANGE, s=60, zorder=5, marker='^', label='Impulse gate (×3)')
    ax.scatter(dod_v[harvest_idx[:9],0], dod_v[harvest_idx[:9],1], dod_v[harvest_idx[:9],2],
               color='#00ccff', s=40, zorder=5, marker='s', label='Harvest gate (×9)')
    
    lim = scale*1.7
    ax.set_xlim(-lim,lim); ax.set_ylim(-lim,lim); ax.set_zlim(-lim,lim)
    ax.set_xlabel('X (mm)',color='#666'); ax.set_ylabel('Y (mm)',color='#666'); ax.set_zlabel('Z (mm)',color='#666')
    ax.tick_params(colors='#555',labelsize=7)
    for p in [ax.xaxis.pane,ax.yaxis.pane,ax.zaxis.pane]: p.set_facecolor((0,0,0,0))
    ax.set_title('CUBIX-ICODED — CAD Geometry\nRotor (Icosahedron, blue) + Stator (Dodecahedron, green)',
                 color='white', fontsize=11, pad=10)
    legend = ax.legend(loc='upper left', facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=7)
    
    # Top-right: layer cross section
    ax2 = fig.add_subplot(2,2,2)
    ax2.set_facecolor('#0a0e1a')
    ax2.set_aspect('equal')
    layers = [
        (165, '#3a3a5a', 'Ti Frame'),
        (145, '#1a4a3a', 'EMF Shield'),
        (118, '#1a2a5a', 'Stator'),
        (90,  '#3a1a4a', 'Rotor'),
        (28,  '#5a2a1a', 'Bi Core'),
    ]
    colors_l = [PURPLE, GREEN, BLUE, '#cc44ff', ORANGE]
    for (r,fc,lbl), col in zip(reversed(layers), reversed(colors_l)):
        circle = plt.Circle((0,0), r, color=fc, alpha=0.9, ec=col, lw=1.2)
        ax2.add_patch(circle)
    for (r,fc,lbl), col in zip(layers, colors_l):
        ax2.text(r*0.62, 0, lbl, ha='center', color=col, fontsize=6.5, fontweight='bold')
    ax2.annotate('Air gap\n0.30mm', xy=(90,5), xytext=(100,40),
                 color=YELLOW, fontsize=6.5,
                 arrowprops=dict(arrowstyle='->', color=YELLOW, lw=0.8))
    ax2.set_xlim(-180,200); ax2.set_ylim(-170,170)
    ax2.axis('off')
    ax2.set_title('Cross-Section (to scale)', color='white', fontsize=9, pad=6)
    
    # Bottom-right: specs table
    ax3 = fig.add_subplot(2,2,4)
    ax3.set_facecolor('#0a0e1a')
    ax3.axis('off')
    specs = [
        ['Parameter','Value'],
        ['Rotor shape','Icosahedron (20 faces)'],
        ['Edge length','115.34 mm'],
        ['Bevel angle','20.905°'],
        ['Stator shape','Dodecahedron (12 ports)'],
        ['Air gap','0.30 mm target'],
        ['Magnets','60× SmCo N52 (25×10×5mm)'],
        ['Clusters','12× Halbach 4:1 star'],
        ['Phase offset','31.71°'],
        ['Target RPM','25,000'],
        ['Core material','Bi 99.99% (diamagnetic)'],
        ['Frame','Ti Grade 5 / 330mm'],
    ]
    for row_i, (k,v) in enumerate(specs):
        y = 1.0 - row_i*0.077
        if row_i == 0:
            ax3.text(0.0, y, k, transform=ax3.transAxes, color=BLUE, fontsize=8, fontweight='bold')
            ax3.text(0.5, y, v, transform=ax3.transAxes, color=BLUE, fontsize=8, fontweight='bold')
            ax3.axhline(y=y-0.01, xmin=0, xmax=1, color='#334', lw=0.8)
        else:
            col = 'white' if row_i%2==0 else '#bbbbbb'
            ax3.text(0.0, y, k+':', transform=ax3.transAxes, color='#888', fontsize=7.5)
            ax3.text(0.5, y, v, transform=ax3.transAxes, color=col, fontsize=7.5)
    ax3.set_title('Technical Specifications', color='white', fontsize=9, pad=6)
    
    plt.suptitle('CUBIX-ICODED — Phase 1 CAD & Architecture Overview\nBojan Sebastian Andrei · Cluj-Napoca, Romania',
                 color='white', fontsize=12, y=1.01)
    plt.tight_layout()
    plt.savefig(OUT+'CUBIX_CAD_3D.png', dpi=200, bbox_inches='tight', facecolor=DARK)
    print("✓ CAD_3D saved")

# ── FIG 2: Magnetic Flux ──

def fig_magnetic_flux():
    TH, RR, B = compute_flux_grid()
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.patch.set_facecolor(DARK)
    
    # 2D flux density heatmap (polar)
    ax1 = fig.add_subplot(131, projection='polar')
    ax1.set_facecolor('#0a0e1a')
    pcm = ax1.pcolormesh(TH, RR*1000, B, cmap='inferno', shading='auto')
    ax1.set_ylim(0, STATOR_R*1000*1.05)
    ax1.set_title('Flux Density B (T)\nRotor-Stator Gap', color='white', fontsize=10, pad=15)
    cb = plt.colorbar(pcm, ax=ax1, fraction=0.04, pad=0.08)
    cb.ax.tick_params(colors='#888', labelsize=7)
    cb.set_label('B (T)', color='#888', fontsize=8)
    
    # 1D Halbach field profile
    ax2 = fig.add_subplot(132)
    ax2.set_facecolor('#0a0e1a')
    theta_1d = np.linspace(0, 2*np.pi, 720)
    B_in, B_out = halbach_field_1d(theta_1d)
    ax2.plot(np.degrees(theta_1d), B_in, color=BLUE, lw=1.5, label='Inner (Halbach ×4)')
    ax2.plot(np.degrees(theta_1d), B_out, color=RED, lw=1.0, alpha=0.6, label='Outer (×1)')
    ax2.axhline(y=np.mean(B_in), color=YELLOW, lw=0.8, linestyle='--', alpha=0.7, label=f'Mean inner: {np.mean(B_in):.2f}T')
    ax2.fill_between(np.degrees(theta_1d), B_in, alpha=0.15, color=BLUE)
    style_ax(ax2, 'Halbach Field Profile\n(12 clusters, 4:1 asymmetry)', 'θ (°)', 'B (T)')
    ax2.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=7)
    ax2.set_xticks([0,90,180,270,360])
    
    # Flux linkage per gate
    ax3 = fig.add_subplot(133)
    ax3.set_facecolor('#0a0e1a')
    gate_angles = []
    gate_labels = []
    gate_flux = []
    gate_colors = []
    for i,ang in enumerate([0,120,240]):
        gate_angles.append(ang)
        gate_labels.append(f'I{i+1}')
        gate_colors.append(ORANGE)
        B_in, _ = halbach_field_1d(np.array([np.radians(ang)]))
        gate_flux.append(float(B_in[0]) * np.pi*(17.5e-3)**2 * 80)  # N·Φ
    idx=1
    for base in [0,120,240]:
        for delta in [OFFSET_DEG, OFFSET_DEG*2, OFFSET_DEG*3]:
            ang = base+delta
            gate_angles.append(ang)
            gate_labels.append(f'H{idx}')
            gate_colors.append('#00ccff' if idx<=3 else GREEN if idx<=6 else PURPLE)
            B_in, _ = halbach_field_1d(np.array([np.radians(ang)]))
            gate_flux.append(float(B_in[0])*np.pi*(17.5e-3)**2*120)
            idx+=1
    
    bars = ax3.bar(range(12), gate_flux, color=gate_colors, alpha=0.85, edgecolor='#334', lw=0.5)
    ax3.set_xticks(range(12))
    ax3.set_xticklabels(gate_labels, color='#aaa', fontsize=7, rotation=45)
    style_ax(ax3, 'Flux Linkage per Gate (Wb·turns)', 'Gate', 'NΦ (Wb·turns)')
    
    plt.suptitle('CUBIX-ICODED — Magnetic Simulation', color='white', fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT+'CUBIX_Magnetic_Sim.png', dpi=200, bbox_inches='tight', facecolor=DARK)
    print("✓ Magnetic_Sim saved")

# ── FIG 3: Torque, EMF, Efficiency ──

def fig_dynamics():
    rpm, T_net, T_fric, T_em, EMF_h, eff = torque_vs_rpm()
    t, impulse, harvest = gate_emf_phase()
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.patch.set_facecolor(DARK)
    
    # Torque vs RPM
    ax = axes[0,0]
    ax.set_facecolor('#0a0e1a')
    ax.plot(rpm/1000, T_em, color=BLUE, lw=2, label='Electromagnetic torque')
    ax.plot(rpm/1000, np.maximum(T_net,0), color=GREEN, lw=2, label='Net torque')
    ax.plot(rpm/1000, T_fric, color=RED, lw=1.5, linestyle='--', label='Friction losses')
    ax.fill_between(rpm/1000, np.maximum(T_net,0), alpha=0.12, color=GREEN)
    ax.axvline(x=3, color=YELLOW, lw=0.8, linestyle=':', alpha=0.7, label='Phase 1 target (3k RPM)')
    ax.axvline(x=25, color=ORANGE, lw=0.8, linestyle=':', alpha=0.7, label='Final target (25k RPM)')
    style_ax(ax, 'Torque vs RPM', 'RPM (×1000)', 'Torque (N·m)')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=7)
    ax.set_xlim(0,30)
    
    # Back-EMF vs RPM
    ax = axes[0,1]
    ax.set_facecolor('#0a0e1a')
    ax.plot(rpm/1000, EMF_h, color=PURPLE, lw=2, label='Total harvest EMF (9 coils)')
    ax.plot(rpm/1000, EMF_h/9, color='#00ccff', lw=1.5, linestyle='--', label='Per-coil EMF')
    ax.axhline(y=12, color=YELLOW, lw=0.8, linestyle=':', alpha=0.7, label='12V reference')
    ax.axhline(y=48, color=ORANGE, lw=0.8, linestyle=':', alpha=0.7, label='48V reference')
    style_ax(ax, 'Back-EMF vs RPM', 'RPM (×1000)', 'EMF (V)')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=7)
    ax.set_xlim(0,30); ax.set_ylim(0)
    
    # Efficiency
    ax = axes[0,2]
    ax.set_facecolor('#0a0e1a')
    ax.plot(rpm/1000, eff*100, color=GREEN, lw=2)
    ax.fill_between(rpm/1000, eff*100, alpha=0.15, color=GREEN)
    style_ax(ax, 'Mechanical Efficiency vs RPM', 'RPM (×1000)', 'Efficiency (%)')
    ax.set_xlim(0,30); ax.set_ylim(0,105)
    ax.axhline(y=80, color=YELLOW, lw=0.8, linestyle='--', alpha=0.6, label='80% reference')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=7)
    
    # Impulse gate waveforms
    ax = axes[1,0]
    ax.set_facecolor('#0a0e1a')
    cols_i = [ORANGE, '#ff9900', '#ffcc00']
    for (lbl, sig), col in zip(impulse.items(), cols_i):
        ax.plot(t*1000, sig, color=col, lw=1.5, label=lbl, alpha=0.9)
    style_ax(ax, 'Impulse Gate EMF Waveforms\n(3000 RPM)', 'Time (ms)', 'EMF (V)')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=8)
    
    # Harvesting gate waveforms (3 triplets)
    ax = axes[1,1]
    ax.set_facecolor('#0a0e1a')
    triplet_cols = ['#00ccff','#0099cc','#006699',
                    GREEN,'#00cc77','#009955',
                    PURPLE,'#8866cc','#664499']
    for (lbl, sig), col in zip(harvest.items(), triplet_cols):
        ax.plot(t*1000, sig, color=col, lw=1.2, label=lbl, alpha=0.85)
    style_ax(ax, 'Harvesting Gate EMF Waveforms\n(3000 RPM, 31.71° offset visible)', 'Time (ms)', 'EMF (V)')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=6,
              ncol=3, loc='upper right')
    
    # Phase offset diagram
    ax = axes[1,2]
    ax.set_facecolor('#0a0e1a')
    theta = np.linspace(0, 2*np.pi, 720)
    ax.plot(np.degrees(theta), np.sin(theta), color=ORANGE, lw=2, label='I1 (0°)', alpha=0.9)
    ax.plot(np.degrees(theta), np.sin(theta - np.radians(OFFSET_DEG)), color='#00ccff', lw=2,
            label=f'H1 (+{OFFSET_DEG}°)', alpha=0.9)
    ax.plot(np.degrees(theta), np.sin(theta - np.radians(OFFSET_DEG*2)), color=GREEN, lw=1.5,
            label=f'H2 (+{OFFSET_DEG*2:.1f}°)', alpha=0.7)
    ax.axvline(x=OFFSET_DEG, color=YELLOW, lw=0.8, linestyle='--', alpha=0.6)
    ax.text(OFFSET_DEG+2, 0.85, f'{OFFSET_DEG}°', color=YELLOW, fontsize=8)
    style_ax(ax, f'Phase Offset Detail\nImpulse vs Harvesting ({OFFSET_DEG}°)', 'θ (°)', 'Normalized EMF')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=8)
    ax.set_xticks([0,90,180,270,360])
    
    plt.suptitle('CUBIX-ICODED — Electromagnetic Dynamics Simulation', color='white', fontsize=13)
    plt.tight_layout()
    plt.savefig(OUT+'CUBIX_Dynamics_Sim.png', dpi=200, bbox_inches='tight', facecolor=DARK)
    print("✓ Dynamics_Sim saved")

# ── FIG 4: Structural Analysis ──

def fig_structural():
    rpm, sigma, F_cent, SF = rotor_stress_vs_rpm()
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.patch.set_facecolor(DARK)
    
    # Hoop stress
    ax = axes[0]
    ax.set_facecolor('#0a0e1a')
    ax.plot(rpm/1000, sigma, color=RED, lw=2)
    ax.fill_between(rpm/1000, sigma, alpha=0.15, color=RED)
    ax.axhline(y=180, color=YELLOW, lw=1.5, linestyle='--', label='PEEK-CF yield (180 MPa)')
    ax.axhline(y=90, color=ORANGE, lw=1, linestyle=':', label='50% yield (safety)')
    ax.axvline(x=25, color=BLUE, lw=0.8, linestyle=':', label='25k RPM target')
    style_ax(ax, 'Rotor Hoop Stress (PEEK-CF)\nvs RPM', 'RPM (×1000)', 'σ_hoop (MPa)')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=8)
    ax.set_xlim(0,30)
    
    # Safety factor
    ax = axes[1]
    ax.set_facecolor('#0a0e1a')
    ax.plot(rpm/1000, np.minimum(SF, 20), color=GREEN, lw=2)
    ax.fill_between(rpm/1000, np.minimum(SF,20), alpha=0.12, color=GREEN)
    ax.axhline(y=3, color=YELLOW, lw=1.2, linestyle='--', label='SF=3 (engineering minimum)')
    ax.axhline(y=1.5, color=RED, lw=1, linestyle='--', label='SF=1.5 (critical)')
    ax.axvline(x=25, color=BLUE, lw=0.8, linestyle=':')
    style_ax(ax, 'Safety Factor vs RPM\n(PEEK-CF Rotor Panel)', 'RPM (×1000)', 'Safety Factor')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=8)
    ax.set_xlim(0,30); ax.set_ylim(0,20)
    
    # Centrifugal force on magnets
    ax = axes[2]
    ax.set_facecolor('#0a0e1a')
    ax.plot(rpm/1000, F_cent, color=PURPLE, lw=2, label='Per SmCo magnet')
    ax.plot(rpm/1000, F_cent*5, color='#ff88aa', lw=1.5, linestyle='--', label='Per cluster (×5)')
    ax.fill_between(rpm/1000, F_cent, alpha=0.15, color=PURPLE)
    ax.axvline(x=25, color=BLUE, lw=0.8, linestyle=':', label='25k RPM target')
    # Loctite EA9492 shear strength: ~28 MPa, contact area ~1250mm²
    F_bond = 28e6 * 25e-3 * 10e-3
    ax.axhline(y=F_bond, color=ORANGE, lw=1.2, linestyle='--', label=f'Bond limit: {F_bond:.0f}N')
    style_ax(ax, 'Centrifugal Force on Magnets\n(SmCo, Loctite EA9492 bond)', 'RPM (×1000)', 'Force (N)')
    ax.legend(facecolor='#111122', edgecolor='#334', labelcolor='white', fontsize=7)
    ax.set_xlim(0,30)
    
    plt.suptitle('CUBIX-ICODED — Structural Integrity Analysis', color='white', fontsize=13)
    plt.tight_layout()
    plt.savefig(OUT+'CUBIX_Structural_Sim.png', dpi=200, bbox_inches='tight', facecolor=DARK)
    print("✓ Structural_Sim saved")

# ── EXPORT CAD JSON ──

def export_cad_json():
    scale = EDGE_MM/2
    ico_v = icosahedron_vertices(scale).tolist()
    ico_f = icosahedron_faces(icosahedron_vertices(scale))
    dod_v = dodecahedron_vertices(scale*1.3).tolist()
    
    # Magnet positions & orientations
    magnets = []
    for vi, v in enumerate(ico_v):
        v = np.array(v)
        rad = v/np.linalg.norm(v)
        perp = np.cross(rad,[0,0,1])
        if np.linalg.norm(perp)<0.01: perp=np.cross(rad,[0,1,0])
        perp/=np.linalg.norm(perp)
        for k in range(5):
            angle=2*np.pi*k/5
            rot=perp*np.cos(angle)+np.cross(rad,perp)*np.sin(angle)
            pos=(v+rot*(scale*0.22)).tolist()
            magnets.append({
                "cluster": vi+1,
                "magnet": k+1,
                "position_mm": [round(p,3) for p in pos],
                "orientation": [round(r,4) for r in rot.tolist()],
                "type": "SmCo_N52_25x10x5mm"
            })
    
    # Stator gates
    gates = []
    for i,ang in enumerate([0,120,240]):
        gates.append({"id":f"I{i+1}","type":"impulse","angle_deg":ang,"coil_turns":80})
    idx=1
    for base in [0,120,240]:
        for delta in [OFFSET_DEG,OFFSET_DEG*2,OFFSET_DEG*3]:
            gates.append({"id":f"H{idx}","type":"harvest","angle_deg":round(base+delta,2),"coil_turns":120})
            idx+=1
    
    data = {
        "project": "CUBIX-ICODED",
        "version": "v0.3-sim",
        "author": "Bojan Sebastian Andrei",
        "units": "mm",
        "rotor": {
            "shape": "icosahedron",
            "edge_length_mm": EDGE_MM,
            "bevel_angle_deg": BEVEL_DEG,
            "vertices_count": len(ico_v),
            "faces_count": len(ico_f),
            "vertices": [[round(x,3) for x in v] for v in ico_v],
            "faces": ico_f
        },
        "stator": {
            "shape": "dodecahedron",
            "vertices_count": len(dod_v),
            "vertices": [[round(x,3) for x in v] for v in dod_v],
            "phase_offset_deg": OFFSET_DEG,
            "gates": gates
        },
        "magnets": magnets,
        "simulation_params": {
            "air_gap_mm": 0.30,
            "rotor_radius_mm": ROTOR_R*1000,
            "stator_radius_mm": STATOR_R*1000,
            "Br_Tesla": MAGNET_BR,
            "target_rpm_phase1": 3000,
            "target_rpm_final": 25000
        }
    }
    
    with open(OUT+'CUBIX_CAD_data.json','w') as f:
        json.dump(data, f, indent=2)
    print("✓ CAD JSON exported")
    return data

# ── MAIN ──

print("\n CUBIX-ICODED — Simulation Engine")
print("="*40)

cad_data = export_cad_json()
print(f" Rotor vertices: {len(cad_data['rotor']['vertices'])}")
print(f" Stator gates: {len(cad_data['stator']['gates'])}")
print(f" Total magnets: {len(cad_data['magnets'])}")

print("\nGenerating figures...")
fig_cad_3d()
fig_magnetic_flux()
fig_dynamics()
fig_structural()

print("\n✅ All simulations complete!")
print(f" Output: {OUT}")
