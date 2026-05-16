// =====================================================
// cubix_rotor.scad — Icosahedral Rotor
// CUBIX-ICODED | Phase 0 Geometry
// =====================================================
// Material: PEEK-CF panels, 5 mm thick, 20.905° bevel
// Magnets:  60× SmCo 25×10×5 mm in 12 Halbach clusters
//           (5 magnets / vertex, pentagonal-star arrangement)
// Shaft:    Ø30 mm bore with 8×4 mm keyway
// =====================================================

include <cubix_params.scad>

// ─── ICOSAHEDRON VERTICES (edge = ROTOR_EDGE) ─────────
function _s() = ROTOR_EDGE / 2;

function ico_verts() = let(s=_s(), p=PHI) [
    s*[ 0,  1,  p],  // v0  — top pole
    s*[ 0, -1,  p],  // v1
    s*[ 0,  1, -p],  // v2
    s*[ 0, -1, -p],  // v3  — bottom pole
    s*[ 1,  p,  0],  // v4
    s*[-1,  p,  0],  // v5
    s*[ 1, -p,  0],  // v6
    s*[-1, -p,  0],  // v7
    s*[ p,  0,  1],  // v8
    s*[-p,  0,  1],  // v9
    s*[ p,  0, -1],  // v10
    s*[-p,  0, -1]   // v11
];

// ─── 20 TRIANGULAR FACES (CCW from outside) ───────────
function ico_faces() = [
    // Top cap (around v0)
    [0,1,8], [0,8,4], [0,4,5], [0,5,9], [0,9,1],
    // Bottom cap (around v3)
    [3,10,2], [3,6,10], [3,7,6], [3,11,7], [3,2,11],
    // Middle belt
    [1,6,8], [6,10,8], [8,10,4], [10,2,4], [4,2,5],
    [2,11,5], [5,11,9], [11,7,9], [9,7,1], [1,7,6]
];

// ─── HOLLOW ICOSAHEDRAL SHELL ─────────────────────────
module ico_shell() {
    inner_s = 1 - (2 * ROTOR_WALL / ROTOR_EDGE);
    difference() {
        polyhedron(points=ico_verts(), faces=ico_faces(), convexity=4);
        scale([inner_s, inner_s, inner_s])
            polyhedron(points=ico_verts(), faces=ico_faces(), convexity=4);
        // Central shaft bore + keyway
        shaft_bore();
    }
}

// ─── SHAFT BORE WITH KEYWAY ───────────────────────────
module shaft_bore() {
    L = ROTOR_EDGE * 2.5;
    union() {
        cylinder(h=L, d=SHAFT_D + SHAFT_TOL*2, center=true);
        // Keyway slot
        translate([SHAFT_D/2 - KEYWAY_H/2, 0, 0])
            cube([KEYWAY_H + SHAFT_TOL, KEYWAY_W + SHAFT_TOL, L], center=true);
    }
}

// ─── SINGLE MAGNET POCKET ─────────────────────────────
// Oriented so MAG_D is along +Z (radial = outward)
module magnet_pocket() {
    cube([MAG_L + MAG_CLEAR,
          MAG_W + MAG_CLEAR,
          MAG_D + MAG_CLEAR + $eps], center=true);
}

// ─── HALBACH PENTAGONAL STAR CLUSTER ──────────────────
// 5 pockets arranged 72° apart around the radial direction
// r_ring = radial distance from vertex to pocket center
module halbach_cluster(r_ring=3.5) {
    for (i = [0:4]) {
        a = 72 * i;
        rotate([0, 0, a])
        translate([r_ring + MAG_L/2, 0, 0])
        rotate([0, 90, 0])          // MAG_D now along radial
            magnet_pocket();
    }
}

// ─── PLACE CLUSTERS AT ALL 12 VERTICES ────────────────
// Uses rotation-axis/angle to align +Z to each vertex direction
module place_clusters() {
    verts = ico_verts();
    for (v = verts) {
        r = norm(v);
        dir = v / r;
        ax  = cross([0,0,1], dir);
        ang = acos(min(1, max(-1, dir[2])));
        translate(v - dir * (MAG_D/2))   // pocket flush with surface
        rotate(a=ang,
               v=(norm(ax) > 0.001 ? ax/norm(ax) : [1,0,0]))
            halbach_cluster();
    }
}

// ─── BEVEL RING AT EACH EDGE (visual guide) ───────────
// Approximate chamfer indicator — cosmetic only
module edge_bevel_guides() {
    verts = ico_verts();
    faces = ico_faces();
    %for (f = faces) {
        for (k = [0:2]) {
            v0 = verts[f[k]];
            v1 = verts[f[(k+1)%3]];
            mid = (v0+v1)/2;
            dir = v1-v0;
            rotate(a=acos(dir[2]/norm(dir)),
                   v=cross([0,0,1],dir))
            translate(mid)
                rotate([90,0,0])
                    cylinder(h=norm(dir), d=0.8, center=true, $fn=8);
        }
    }
}

// ─── COMPLETE ROTOR ────────────────────────────────────
module cubix_rotor() {
    difference() {
        ico_shell();
        place_clusters();
    }
}

// ─── RENDER ────────────────────────────────────────────
color("SteelBlue", 0.92)
    cubix_rotor();

// Reference axis (ghost, rendered with %)
%color("crimson")
    cylinder(h=ROTOR_EDGE*1.6, d=1, center=true);

// ─── ECHO GEOMETRY ────────────────────────────────────
echo(str("Rotor edge:           ", ROTOR_EDGE,   " mm"));
echo(str("Rotor circumradius:   ", ROTOR_CIRCUM, " mm"));
echo(str("Rotor wall thickness: ", ROTOR_WALL,   " mm"));
echo(str("Magnet clusters:      ", NUM_CLUSTERS));
echo(str("Magnets total:        ", NUM_CLUSTERS * MAG_PER_CLUSTER));
echo(str("Bevel angle:          ", ROTOR_BEVEL,  " deg"));
