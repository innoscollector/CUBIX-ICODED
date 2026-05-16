// =====================================================
// cubix_core.scad — Pentagonal Bipyramidal Core
// CUBIX-ICODED | Phase 0 Geometry
// =====================================================
// Bismuth core: 99.99% purity, μr ≈ 0.99983 (diamagnetic)
//   → repels magnetic fields passively, no supercooling needed
//   → low melting point (271°C): use sharp carbide, no coolant flood
// PEEK cage: non-conductive, non-magnetic support skeleton
//   → 5 equatorial windows for flux interaction
//   → M3 nylon mount screws at 5 positions
//
// Phase 1 option: replace Bismuth with PTFE dummy core
//   (same geometry, zero fracture risk during spin-up tests)
// =====================================================

include <cubix_params.scad>

// ─── BIPYRAMID VERTICES ───────────────────────────────
// r = equatorial radius, h = half-height (apex distance)
function bpy_verts(r=CORE_R, h=CORE_H) = concat(
    [ for (i=[0:4]) [r*cos(72*i), r*sin(72*i), 0] ],  // v0–v4 equatorial
    [[0, 0,  h]],                                       // v5 top apex
    [[0, 0, -h]]                                        // v6 bottom apex
);

// ─── 10 TRIANGULAR FACES (CCW from outside) ───────────
function bpy_faces() = [
    // Top pyramid (apex = v5)
    [0,5,1], [1,5,2], [2,5,3], [3,5,4], [4,5,0],
    // Bottom pyramid (apex = v6) — reversed winding
    [1,6,0], [2,6,1], [3,6,2], [4,6,3], [0,6,4]
];

// ─── SOLID BISMUTH CORE ───────────────────────────────
module bismuth_core() {
    color("#b87333", 0.95)   // Bismuth iridescent approximation
    polyhedron(
        points = bpy_verts(r=CORE_R, h=CORE_H),
        faces  = bpy_faces(),
        convexity = 3
    );
}

// ─── PEEK SUPPORT CAGE ────────────────────────────────
module peek_cage() {
    r_o = CORE_R + CORE_WALL;
    h_o = CORE_H + CORE_WALL;
    r_i = CORE_R + 0.1;    // 0.1 mm bismuth clearance
    h_i = CORE_H + 0.1;

    color("ivory", 0.8)
    difference() {
        // Outer cage bipyramid
        polyhedron(points=bpy_verts(r=r_o, h=h_o),
                   faces=bpy_faces(), convexity=3);
        // Inner void (bismuth space)
        polyhedron(points=bpy_verts(r=r_i, h=h_i),
                   faces=bpy_faces(), convexity=3);
        // Shaft bore
        cylinder(h=(h_o+1)*2, d=SHAFT_D, center=true, $fn=36);
        // 5 equatorial flux windows (spherical cutouts)
        for (i=[0:4])
            rotate([0,0,72*i])
            translate([r_o-1, 0, 0])
                sphere(r=7, $fn=16);
        // 5 M3 nylon mount holes (offset 36° from windows)
        for (i=[0:4])
            rotate([0,0,72*i+36])
            translate([(r_o+r_i)/2, 0, 0])
                cylinder(h=(h_o+2)*2, d=3.3, center=true, $fn=12);
    }
}

// ─── COMPLETE CORE ASSEMBLY ───────────────────────────
module cubix_core() {
    bismuth_core();
    peek_cage();
}

// ─── PHASE 1 DUMMY (PTFE substitute) ──────────────────
module cubix_core_ptfe_dummy() {
    color("white", 0.9)
    polyhedron(
        points = bpy_verts(r=CORE_R, h=CORE_H),
        faces  = bpy_faces(),
        convexity = 3
    );
    peek_cage();
}

// ─── RENDER (change to cubix_core_ptfe_dummy() for Phase 1) ──
cubix_core();
// cubix_core_ptfe_dummy();  // ← uncomment for Phase 1 safe testing

// Axis reference
%color("crimson")
    cylinder(h=CORE_H*4, d=1, center=true);

// ─── ECHO GEOMETRY ────────────────────────────────────
echo(str("Core equatorial R: ", CORE_R, " mm"));
echo(str("Core half-height:  ", CORE_H, " mm"));
echo(str("PEEK cage wall:    ", CORE_WALL, " mm"));
echo(str("Shaft bore Ø:      ", SHAFT_D, " mm"));
echo(str("Phase 1 note: Swap bismuth_core() → cubix_core_ptfe_dummy()"));
