// =====================================================
// cubix_stator.scad — Dodecahedral Stator
// CUBIX-ICODED | Phase 0 Geometry
// =====================================================
// Material: PEEK / FR4 G10 pentagonal panels + PEEK-CF inserts
// Gates:    12 total — 3 impulse (I1–I3) + 9 harvesting (H1–H9)
// Coil bore: Ø35 mm × 18 mm deep at each pentagonal face center
// Phase offset: 31.71° between impulse and harvest gate vectors
// Support ring: Ø280 mm × 10 mm Al6061, concentric mount
// =====================================================

include <cubix_params.scad>

// ─── DODECAHEDRON RAW VERTICES (edge ≈ 2/PHI) ─────────
function _dv() = let(p=PHI, ip=1/PHI) [
    [ 1,  1,  1], [ 1,  1, -1], [ 1, -1,  1], [ 1, -1, -1],  // v0–v3
    [-1,  1,  1], [-1,  1, -1], [-1, -1,  1], [-1, -1, -1],  // v4–v7
    [ 0, ip,  p], [ 0,-ip,  p], [ 0, ip, -p], [ 0,-ip, -p],  // v8–v11
    [ ip,  p,  0],[-ip,  p,  0],[ ip, -p,  0],[-ip, -p,  0], // v12–v15
    [ p,  0, ip], [ p,  0,-ip],[-p,  0, ip], [-p,  0,-ip]    // v16–v19
];

// ─── 12 PENTAGONAL FACES (CCW from outside) ───────────
// Faces 0–2:  Impulse gates  I1, I2, I3
// Faces 3–11: Harvesting gates H1–H9
function dode_faces() = [
    [0, 8, 4,13,12],   // f0  I1 — +Z dominant
    [0,12, 1,17,16],   // f1  I2
    [0,16, 2, 9, 8],   // f2  I3
    [1,10, 5,13,12],   // f3  H1
    [1,17, 3,11,10],   // f4  H2
    [2,14, 3,17,16],   // f5  H3
    [2, 9, 6,15,14],   // f6  H4
    [4, 8, 9, 6,18],   // f7  H5
    [4,18,19, 5,13],   // f8  H6
    [5,19, 7,11,10],   // f9  H7
    [6,15, 7,19,18],   // f10 H8
    [3,14,15, 7,11]    // f11 H9
];

// ─── SCALE TO DESIRED INRADIUS ─────────────────────────
// Face 0 centroid → raw inradius → scale to STATOR_INRAD
function _dode_scale() =
    let(rv = _dv(), f0 = dode_faces()[0],
        fc = (rv[f0[0]]+rv[f0[1]]+rv[f0[2]]+rv[f0[3]]+rv[f0[4]])/5)
    STATOR_INRAD / norm(fc);

function dode_verts() =
    let(s = _dode_scale()) [ for (v = _dv()) s*v ];

// ─── FACE CENTER (for coil bore placement) ────────────
function face_center(fi) =
    let(v = dode_verts(), f = dode_faces()[fi])
    (v[f[0]]+v[f[1]]+v[f[2]]+v[f[3]]+v[f[4]]) / 5;

// ─── HOLLOW DODECAHEDRAL SHELL ─────────────────────────
module dode_shell() {
    inner_s = 1 - (STATOR_WALL / STATOR_INRAD);
    difference() {
        polyhedron(points=dode_verts(), faces=dode_faces(), convexity=6);
        scale([inner_s, inner_s, inner_s])
            polyhedron(points=dode_verts(), faces=dode_faces(), convexity=6);
        // Shaft + rotor clearance bore
        cylinder(h=STATOR_INRAD*3, d=SHAFT_D+8, center=true);
    }
}

// ─── COIL GATE BORE at face index fi ──────────────────
module coil_bore(fi) {
    fc  = face_center(fi);
    dir = fc / norm(fc);
    ax  = cross([0,0,1], dir);
    ang = acos(min(1, max(-1, dir[2])));
    translate(fc - dir * $eps)
    rotate(a=ang, v=(norm(ax)>0.001 ? ax/norm(ax) : [1,0,0]))
        cylinder(h=COIL_BORE_DEPTH + $eps*2, d=COIL_BORE_D, $fn=36);
}

// ─── CUT ALL 12 GATE BORES ────────────────────────────
module all_gate_bores() {
    for (fi = [0:11]) coil_bore(fi);
}

// ─── STATOR SUPPORT RING ──────────────────────────────
// Al6061 annular ring, mounted at bottom of stator
module support_ring() {
    d_outer = STATOR_RING_D;
    d_inner = STATOR_RING_D - 40;
    translate([0, 0, -STATOR_INRAD - STATOR_RING_T/2])
    difference() {
        cylinder(h=STATOR_RING_T, d=d_outer, center=true);
        cylinder(h=STATOR_RING_T+1, d=d_inner, center=true);
        // 8× M4 bolt circle
        for (i=[0:7])
            rotate([0,0,45*i])
            translate([(d_outer-16)/2, 0, 0])
                cylinder(h=STATOR_RING_T+2, d=4.3, center=true);
    }
}

// ─── PHASE LABEL INSERTS (visual markers) ─────────────
module gate_markers() {
    // Impulse (orange spheres)
    for (fi=[0:2]) {
        fc = face_center(fi);
        color("orange", 0.85) translate(fc) sphere(r=3.5, $fn=12);
        // Label direction arrows (debug)
        %color("orange") translate(fc) translate(fc/norm(fc)*5)
            sphere(r=1, $fn=8);
    }
    // Harvesting (blue spheres)
    for (fi=[3:11]) {
        fc = face_center(fi);
        color("dodgerblue", 0.85) translate(fc) sphere(r=3.5, $fn=12);
    }
}

// ─── COMPLETE STATOR ───────────────────────────────────
module cubix_stator() {
    difference() {
        union() {
            dode_shell();
            color("Silver", 0.7) support_ring();
        }
        all_gate_bores();
    }
}

// ─── RENDER ────────────────────────────────────────────
color("ForestGreen", 0.55)
    cubix_stator();

gate_markers();

%color("crimson")
    cylinder(h=STATOR_INRAD*1.6, d=1, center=true);

// ─── ECHO GEOMETRY ────────────────────────────────────
echo(str("Stator inradius:  ", STATOR_INRAD, " mm (target)"));
echo(str("Stator edge:      ", STATOR_EDGE,  " mm"));
echo(str("Stator wall:      ", STATOR_WALL,  " mm"));
echo(str("Coil bore Ø:      ", COIL_BORE_D,  " mm"));
echo(str("Coil bore depth:  ", COIL_BORE_DEPTH, " mm"));
echo(str("Phase offset:     ", STATOR_OFFSET,  " deg"));
echo(str("Impulse gates:    ", NUM_IMPULSE));
echo(str("Harvest gates:    ", NUM_HARVEST));
