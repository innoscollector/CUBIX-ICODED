"""
CUBIX-ICODED — Icosahedral Rotor Geometry Visualizer
=====================================================
Author: Bojan Sebastian Andrei (Cluj-Napoca, Romania)
Repo:   https://github.com/innoscollector/CUBIX-ICODED-Experimental-Geometry-Platform
Status: Phase 0 — Digital Geometry Validation

Renders:
  1. Icosahedral rotor with 12 Halbach magnetic star clusters at vertices
  2. Dodecahedral stator with 3 impulse + 9 harvesting gates
  3. Concentric layer diagram (all 5 system layers)

Dependencies:
  pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ─────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────
EDGE_LENGTH_MM      = 115.34          # Icosahedron edge length (mm)
BEVEL_ANGLE_DEG     = 20.905          # Edge chamfer angle (degrees)
STATOR_OFFSET_DEG   = 31.71           # Angular offset between harvesting gates
MAGNETS_PER_CLUSTER = 5
NUM_CLUSTERS        = 12              # One per icosahedron vertex
TOTAL_MAGNETS       = MAGNETS_PER_CLUSTER * NUM_CLUSTERS  # = 60

PHI = (1 + np.sqrt(5)) / 2           # Golden ratio ≈ 1.618

# ─────────────────────────────────────────────────────────────────
# GEOMETRY BUILDERS
# ─────────────────────────────────────────────────────────────────

def icosahedron_vertices(scale=1.0):
    """
    Returns the 12 canonical vertices of a unit icosahedron,
    scaled by `scale` (use edge_length / (2 * sin(2π/5)) for mm).
    """
    verts = []
    for s in [1, -1]:
        for t in [1, -1]:
            verts.append([0,  s,  t * PHI])
            verts.append([s,  t * PHI, 0])
            verts.append([t * PHI, 0, s])
    verts = np.array(verts, dtype=float)
    # Normalize to unit edge length, then scale
    edge = np.linalg.norm(verts[0] - verts[1])
    verts = verts / edge * scale
    return verts


def icosahedron_faces(verts):
    """
    Returns 20 triangular faces as index triples.
    Brute-force: pick all triples whose mutual distance ≈ edge length.
    """
    n = len(verts)
    edge = np.linalg.norm(verts[0] - verts[1])
    tol = edge * 0.01
    faces = []
    for i in range(n):
        for j in range(i+1, n):
            if abs(np.linalg.norm(verts[i] - verts[j]) - edge) < tol:
                for k in range(j+1, n):
                    if (abs(np.linalg.norm(verts[i] - verts[k]) - edge) < tol and
                            abs(np.linalg.norm(verts[j] - verts[k]) - edge) < tol):
                        faces.append([i, j, k])
    return faces


def dodecahedron_vertices(scale=1.0):
    """
    Returns the 20 canonical vertices of a unit dodecahedron.
    Dual of the icosahedron — face centres of the icosahedron.
    """
    verts = []
    for a in [1, -1]:
        for b in [1, -1]:
            for c in [1, -1]:
                verts.append([a, b, c])
    for s in [1, -1]:
        for t in [1, -1]:
            verts.append([0,  s / PHI,  t * PHI])
            verts.append([s / PHI,  t * PHI, 0])
            verts.append([t * PHI, 0, s / PHI])
    verts = np.array(verts, dtype=float)
    edge = min(np.linalg.norm(verts[i] - verts[j])
               for i in range(len(verts)) for j in range(i+1, len(verts)))
    verts = verts / edge * scale
    return verts


# ─────────────────────────────────────────────────────────────────
# FIGURE 1: Icosahedral Rotor + Halbach Clusters
# ─────────────────────────────────────────────────────────────────

def plot_rotor():
    scale = EDGE_LENGTH_MM / 2
    verts = icosahedron_vertices(scale=scale)
    faces = icosahedron_faces(verts)

    fig = plt.figure(figsize=(12, 10))
    fig.patch.set_facecolor('#0d1117')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#0d1117')

    # Draw icosahedral faces
    polys = [[verts[i] for i in f] for f in faces]
    coll = Poly3DCollection(polys, alpha=0.12, linewidths=0.7,
                            edgecolors='#00aaff', facecolors='#1a3a5c')
    ax.add_collection3d(coll)

    # Draw vertices (magnet cluster positions)
    ax.scatter(verts[:, 0], verts[:, 1], verts[:, 2],
               color='#ff4444', s=80, zorder=5, label='Halbach Cluster (×12)')

    # Draw Halbach star arrows at each vertex (5 arrows per cluster)
    arrow_len = scale * 0.28
    for v in verts:
        # Outward radial direction from centre
        radial = v / np.linalg.norm(v)
        # Generate 5 arrows in a pentagonal star around radial axis
        perp = np.cross(radial, [0, 0, 1])
        if np.linalg.norm(perp) < 0.01:
            perp = np.cross(radial, [0, 1, 0])
        perp = perp / np.linalg.norm(perp)
        for k in range(5):
            angle = 2 * np.pi * k / 5
            rot = perp * np.cos(angle) + np.cross(radial, perp) * np.sin(angle)
            tip = v + rot * arrow_len * 0.6
            ax.quiver(v[0], v[1], v[2],
                      rot[0] * arrow_len, rot[1] * arrow_len, rot[2] * arrow_len,
                      color='#ffaa00', alpha=0.7, linewidth=0.8,
                      arrow_length_ratio=0.25)

    # Axis labels & style
    lim = scale * 1.4
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_xlabel('X (mm)', color='#aaaaaa')
    ax.set_ylabel('Y (mm)', color='#aaaaaa')
    ax.set_zlabel('Z (mm)', color='#aaaaaa')
    ax.tick_params(colors='#666666')
    for pane in [ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane]:
        pane.set_facecolor((0, 0, 0, 0))

    ax.set_title(
        f'CUBIX-ICODED — Icosahedral Rotor\n'
        f'Edge: {EDGE_LENGTH_MM} mm | Bevel: {BEVEL_ANGLE_DEG}° | '
        f'{TOTAL_MAGNETS} SmCo magnets in {NUM_CLUSTERS} Halbach clusters',
        color='white', fontsize=11, pad=10
    )

    legend_elements = [
        mpatches.Patch(facecolor='#1a3a5c', edgecolor='#00aaff', label='Icosahedral face (×20, PEEK-CF)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#ff4444',
                   markersize=8, label='Vertex = Halbach star cluster (×12)'),
        plt.Line2D([0], [0], color='#ffaa00', linewidth=1.5,
                   label='Halbach 4:1 projection arrows (×5 per cluster)'),
    ]
    ax.legend(handles=legend_elements, loc='upper left',
              facecolor='#1a1a2e', edgecolor='#333355', labelcolor='white', fontsize=8)

    info = (f"Faces: 20  |  Vertices: 12  |  Edges: 30\n"
            f"Dihedral angle: 138.19°  |  Assembly bevel: {BEVEL_ANGLE_DEG}°\n"
            f"SmCo magnets: {TOTAL_MAGNETS} total  |  Clusters: {NUM_CLUSTERS}")
    ax.text2D(0.02, 0.02, info, transform=ax.transAxes,
              color='#888888', fontsize=7.5, verticalalignment='bottom',
              bbox=dict(boxstyle='round', facecolor='#111111', alpha=0.7))

    plt.tight_layout()
    plt.savefig('CUBIX_rotor_icosahedron.png', dpi=180,
                bbox_inches='tight', facecolor='#0d1117')
    print("  ✓ Saved: CUBIX_rotor_icosahedron.png")
    return fig


# ─────────────────────────────────────────────────────────────────
# FIGURE 2: Dodecahedral Stator — Gate Map
# ─────────────────────────────────────────────────────────────────

def plot_stator_gate_map():
    """
    2D polar diagram of the 12 stator gates:
    3 impulse (I1–I3) and 9 harvesting (H1–H9), with the 31.71° offset.
    """
    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(projection='polar'))
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')

    # Impulse gates: equally spaced at 0°, 120°, 240°
    impulse_angles = np.radians([0, 120, 240])
    # Harvesting gates: 3 triplets, each offset by STATOR_OFFSET_DEG from impulse
    harvest_angles = []
    for base in [0, 120, 240]:
        for delta in [STATOR_OFFSET_DEG, STATOR_OFFSET_DEG * 2, STATOR_OFFSET_DEG * 3]:
            harvest_angles.append(np.radians(base + delta))
    harvest_angles = np.array(harvest_angles)

    r_gate = 0.75

    # Draw impulse gates
    for idx, angle in enumerate(impulse_angles):
        ax.plot([0, angle], [0, r_gate], color='#ff6600', lw=2.5, alpha=0.9)
        ax.scatter(angle, r_gate, color='#ff6600', s=180, zorder=5)
        ax.text(angle, r_gate + 0.12, f'I{idx+1}',
                ha='center', va='center', color='#ff9944', fontsize=11, fontweight='bold')

    # Draw harvesting gates
    triplet_colors = ['#00ccff', '#00ff99', '#aa88ff']
    for idx, angle in enumerate(harvest_angles):
        color = triplet_colors[idx // 3]
        ax.plot([0, angle], [0, r_gate], color=color, lw=1.8, alpha=0.75)
        ax.scatter(angle, r_gate, color=color, s=130, zorder=5)
        ax.text(angle, r_gate + 0.12, f'H{idx+1}',
                ha='center', va='center', color=color, fontsize=9, fontweight='bold')

    # Mark the 31.71° offset arc on the first triplet
    arc_theta = np.linspace(impulse_angles[0], harvest_angles[0], 60)
    ax.plot(arc_theta, [r_gate * 0.55] * 60, color='#ffff44', lw=1.5, linestyle='--')
    ax.text(np.mean([impulse_angles[0], harvest_angles[0]]), r_gate * 0.43,
            f'{STATOR_OFFSET_DEG}°\noffset', ha='center', color='#ffff44', fontsize=8)

    # Style
    ax.set_ylim(0, 1.0)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines['polar'].set_color('#333333')
    ax.grid(color='#222222', linewidth=0.5)

    ax.set_title(
        f'CUBIX-ICODED — Dodecahedral Stator Gate Map\n'
        f'3 Impulse gates (orange) + 9 Harvesting gates (3 triplets)\n'
        f'Phase offset: {STATOR_OFFSET_DEG}° between impulse and harvesting vectors',
        color='white', fontsize=11, pad=18
    )

    legend_elements = [
        mpatches.Patch(color='#ff6600', label='Impulse gate (I1–I3) — excitation'),
        mpatches.Patch(color='#00ccff', label='Harvesting triplet 1 (H1–H3)'),
        mpatches.Patch(color='#00ff99', label='Harvesting triplet 2 (H4–H6)'),
        mpatches.Patch(color='#aa88ff', label='Harvesting triplet 3 (H7–H9)'),
        plt.Line2D([0], [0], color='#ffff44', linestyle='--', label=f'{STATOR_OFFSET_DEG}° angular offset'),
    ]
    ax.legend(handles=legend_elements, loc='lower left',
              bbox_to_anchor=(-0.15, -0.05),
              facecolor='#1a1a2e', edgecolor='#333355', labelcolor='white', fontsize=8)

    plt.tight_layout()
    plt.savefig('CUBIX_stator_gate_map.png', dpi=180,
                bbox_inches='tight', facecolor='#0d1117')
    print("  ✓ Saved: CUBIX_stator_gate_map.png")
    return fig


# ─────────────────────────────────────────────────────────────────
# FIGURE 3: Concentric Layer Cross-Section
# ─────────────────────────────────────────────────────────────────

def plot_layer_diagram():
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    ax.set_aspect('equal')

    layers = [
        # (radius_mm, color, label, sublabel)
        (165,  '#4a4a6a', 'Layer 1: External Frame',      'Cubic Ti Grade 5 | 330 mm | 8 mm wall'),
        (145,  '#2a5a4a', 'Layer 2: EMF Shielding',        'Rhombic Triacontahedron | Mu-metal'),
        (118,  '#1a3a6a', 'Layer 3: Stator',               'Dodecahedral | 12 coil gates | PEEK-CF'),
        (90,   '#3a1a4a', 'Layer 4: Rotor',                'Icosahedral | 60 SmCo magnets | 0.30 mm gap'),
        (28,   '#5a2a1a', 'Layer 5: Central Core',         'Pentagonal Bipyramidal | Bi 99.99% | Diamagnetic'),
    ]

    for r, color, label, sublabel in reversed(layers):
        circle = plt.Circle((0, 0), r, color=color, alpha=0.85, linewidth=1.5,
                             edgecolor='#aaaacc', fill=True)
        ax.add_patch(circle)

    # Labels with leader lines
    label_x = 20
    for r, color, label, sublabel in layers:
        y_pos = r * 0.72
        ax.annotate(
            f'{label}\n{sublabel}',
            xy=(0, r), xytext=(label_x + 5, y_pos),
            fontsize=7.5, color='white',
            arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#111111', alpha=0.8, edgecolor='#555555'),
        )

    # Air gap annotation
    rotor_r = 90
    stator_r = 118
    ax.annotate('', xy=(rotor_r + 0.3, 0), xytext=(stator_r - 0.3, 0),
                arrowprops=dict(arrowstyle='<->', color='#ffff44', lw=1.5))
    ax.text((rotor_r + stator_r) / 2, 4, 'Air gap\n0.30 mm target',
            ha='center', fontsize=7.5, color='#ffff44')

    # Rotation arrow
    theta = np.linspace(0.2, 1.8 * np.pi, 200)
    rx = 55 * np.cos(theta)
    ry = 55 * np.sin(theta)
    ax.plot(rx, ry, color='#00aaff', lw=2, alpha=0.8)
    ax.annotate('', xy=(rx[-1], ry[-1]),
                xytext=(rx[-2], ry[-2]),
                arrowprops=dict(arrowstyle='->', color='#00aaff', lw=2))
    ax.text(0, -68, '25,000 RPM (target)', ha='center', color='#00aaff', fontsize=8)

    ax.set_xlim(-180, 220)
    ax.set_ylim(-180, 180)
    ax.axis('off')
    ax.set_title(
        'CUBIX-ICODED — Concentric Architecture (Cross-Section)\n5 Functional Layers | Radii to scale',
        color='white', fontsize=12, pad=14
    )

    plt.tight_layout()
    plt.savefig('CUBIX_layer_diagram.png', dpi=180,
                bbox_inches='tight', facecolor='#0d1117')
    print("  ✓ Saved: CUBIX_layer_diagram.png")
    return fig


# ─────────────────────────────────────────────────────────────────
# FIGURE 4: Key Parameters Reference Card
# ─────────────────────────────────────────────────────────────────

def plot_spec_card():
    fig, ax = plt.subplots(figsize=(11, 7))
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    ax.axis('off')

    specs = [
        ('ROTOR GEOMETRY',      [
            ('Shape',                   'Regular Icosahedron'),
            ('Faces',                   '20 equilateral triangles'),
            ('Vertices',                '12 (= magnet cluster positions)'),
            ('Edges',                   '30'),
            ('Edge length',             f'{EDGE_LENGTH_MM} mm'),
            ('Bevel / chamfer angle',   f'{BEVEL_ANGLE_DEG}°'),
            ('Dihedral angle',          '138.19°'),
            ('Material',                'PEEK-CF  (3–8 mm variable)'),
        ]),
        ('MAGNETIC SYSTEM',     [
            ('Magnet type',             'SmCo N52 — 25×10×5 mm'),
            ('Total magnets',           f'{TOTAL_MAGNETS} (60)'),
            ('Clusters',                f'{NUM_CLUSTERS} (one per vertex)'),
            ('Per cluster',             f'{MAGNETS_PER_CLUSTER} magnets — pentagonal star'),
            ('Array type',              'Halbach 4:1 asymmetric projection'),
            ('Core material',           'Bismuth 99.99% (diamagnetic)'),
            ('Air gap target',          '0.30 mm radial clearance'),
        ]),
        ('STATOR SYSTEM',       [
            ('Shape',                   'Regular Dodecahedron'),
            ('Total gates',             '12 (3 impulse + 9 harvesting)'),
            ('Harvesting triplets',     '3 × 3 gates = 9'),
            ('Phase offset',            f'{STATOR_OFFSET_DEG}°'),
            ('Precession tolerance',    '0.02 mm (induced)'),
            ('Gate tolerance',          '±0.005 mm'),
            ('Angular tolerance',       '±0.01°'),
        ]),
        ('OPERATIONAL TARGETS', [
            ('Phase 1 RPM',             '2,000 – 3,000 RPM'),
            ('Validation RPM',          '25,000 RPM'),
            ('Vacuum environment',      '10⁻⁶ Torr'),
            ('Plasma injection',        'Argon / Krypton (Phase 3)'),
            ('Bearing type',            'Ceramic hybrid Si₃N₄'),
            ('Lubrication',             'Krytox GPL 205 (vacuum-rated)'),
        ]),
    ]

    col_width = 0.5
    row_height = 0.072
    col_positions = [0.0, 0.52]

    for col_idx, (title, params) in enumerate(specs):
        x0 = col_positions[col_idx]
        y0 = 0.94

        ax.text(x0 + 0.01, y0, f'▸ {title}', transform=ax.transAxes,
                fontsize=10, fontweight='bold', color='#00aaff', va='top')
        for row_idx, (k, v) in enumerate(params):
            y = y0 - (row_idx + 1) * row_height
            ax.text(x0 + 0.01, y, k + ':', transform=ax.transAxes,
                    fontsize=8, color='#aaaaaa', va='top')
            ax.text(x0 + 0.26, y, v, transform=ax.transAxes,
                    fontsize=8, color='white', va='top')

    ax.set_title(
        'CUBIX-ICODED — Technical Specification Reference Card\n'
        'Bojan Sebastian Andrei · Cluj-Napoca, Romania · Phase 1 Pre-Prototype',
        color='white', fontsize=12, pad=10
    )

    plt.tight_layout()
    plt.savefig('CUBIX_spec_card.png', dpi=180,
                bbox_inches='tight', facecolor='#0d1117')
    print("  ✓ Saved: CUBIX_spec_card.png")
    return fig


# ─────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("\n CUBIX-ICODED Geometry Visualizer")
    print("=" * 42)
    print(f"  Icosahedron edge:       {EDGE_LENGTH_MM} mm")
    print(f"  Bevel angle:            {BEVEL_ANGLE_DEG}°")
    print(f"  Halbach clusters:       {NUM_CLUSTERS}")
    print(f"  Total SmCo magnets:     {TOTAL_MAGNETS}")
    print(f"  Stator phase offset:    {STATOR_OFFSET_DEG}°")
    print(f"  Golden ratio (φ):       {PHI:.6f}")
    print("=" * 42)
    print("\nGenerating figures...")

    fig1 = plot_rotor()
    fig2 = plot_stator_gate_map()
    fig3 = plot_layer_diagram()
    fig4 = plot_spec_card()

    print("\n All figures saved. Add to repo under CAD/Renders/\n")
    plt.show()
