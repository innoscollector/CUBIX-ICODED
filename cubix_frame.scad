// =====================================================
// cubix_frame.scad — Cubic External Frame
// CUBIX-ICODED | Phase 0 Geometry
// =====================================================
// Material: Ti Grade 5 (Ti-6Al-4V), 6 CNC-milled plates
// Outer:    330 × 330 × 330 mm
// Wall:     8 mm
// Features: 12 stator port bores (Ø45 mm),
//           1 access hatch (80×80 mm, Viton O-ring groove),
//           8 corner L-bracket holes,
//           top/bottom shaft feedthrough bores
// =====================================================

include <cubix_params.scad>

// ─── HOLLOW CUBIC SHELL ───────────────────────────────
module frame_shell() {
    difference() {
        cube([FRAME_OUTER, FRAME_OUTER, FRAME_OUTER], center=true);
        cube([FRAME_INNER, FRAME_INNER, FRAME_INNER], center=true);
    }
}

// ─── PORT BORE MODULE ─────────────────────────────────
// Places a cylindrical port bore through the frame wall
module port_bore(pos, normal) {
    depth = FRAME_WALL + 2;
    ax  = cross([0,0,1], normal);
    ang = acos(min(1, max(-1, normal[2])));
    translate(pos)
    rotate(a=ang, v=(norm(ax)>0.001 ? ax/norm(ax) : [1,0,0]))
        cylinder(h=depth*2, d=PORT_D, center=true, $fn=36);
}

// ─── 12 STATOR PORT POSITIONS ─────────────────────────
// 2 ports per cube face × 6 faces = 12 (matching dodecahedral gates)
// Ports are offset ±70 mm from face center to avoid corner regions
module all_port_bores() {
    H = FRAME_OUTER/2 + 1;
    O = 70;   // offset from face center
    // +X face
    port_bore([ H,  O,  O], [1,0,0]);
    port_bore([ H, -O, -O], [1,0,0]);
    // -X face
    port_bore([-H,  O, -O], [-1,0,0]);
    port_bore([-H, -O,  O], [-1,0,0]);
    // +Y face
    port_bore([ O,  H,  O], [0,1,0]);
    port_bore([-O,  H, -O], [0,1,0]);
    // -Y face
    port_bore([ O, -H, -O], [0,-1,0]);
    port_bore([-O, -H,  O], [0,-1,0]);
    // +Z face
    port_bore([ O,  O,  H], [0,0,1]);
    port_bore([-O, -O,  H], [0,0,1]);
    // -Z face
    port_bore([ O, -O, -H], [0,0,-1]);
    port_bore([-O,  O, -H], [0,0,-1]);
}

// ─── ACCESS HATCH (−Y face) ───────────────────────────
// 80×80 mm, with 4 mm O-ring groove
module access_hatch() {
    H = FRAME_OUTER/2 - FRAME_WALL/2;
    translate([0, -FRAME_OUTER/2, 0])
    rotate([90,0,0]) {
        // Main cutout
        cube([HATCH_SIZE, HATCH_SIZE, FRAME_WALL+2], center=true);
        // O-ring groove (2 mm wide, 1.5 mm deep)
        difference() {
            cube([HATCH_SIZE+6, HATCH_SIZE+6, 1.5*2], center=true);
            cube([HATCH_SIZE+2, HATCH_SIZE+2, 1.6*2], center=true);
        }
    }
}

// ─── SHAFT FEEDTHROUGH (top & bottom) ─────────────────
module shaft_feedthrough() {
    cylinder(h=FRAME_OUTER+4, d=SHAFT_D+4, center=true, $fn=36);
}

// ─── CORNER BRACKET HOLES (M6 × 3 per corner) ─────────
// 8 corners × 3 bolt holes = 24 total
module corner_bracket_holes() {
    for (sx=[-1,1]) for (sy=[-1,1]) for (sz=[-1,1]) {
        x = sx*(FRAME_OUTER/2 - 14);
        y = sy*(FRAME_OUTER/2 - 14);
        z = sz*(FRAME_OUTER/2 - 14);
        translate([x,y,z]) {
            cylinder(h=FRAME_WALL+4, d=M6_BORE, center=true);
            rotate([90,0,0]) cylinder(h=FRAME_WALL+4, d=M6_BORE, center=true);
            rotate([0,90,0]) cylinder(h=FRAME_WALL+4, d=M6_BORE, center=true);
        }
    }
}

// ─── VIEWPORT WINDOW HOLES (×2, KF40 flange) ─────────
// Optical access for laser tachometer / inspection
module viewport_holes() {
    // +X and -X faces for cross-beam optical path
    translate([ FRAME_OUTER/2, 0, 0])
        rotate([0,90,0]) cylinder(h=FRAME_WALL+2, d=40, center=true, $fn=36);
    translate([-FRAME_OUTER/2, 0, 0])
        rotate([0,90,0]) cylinder(h=FRAME_WALL+2, d=40, center=true, $fn=36);
}

// ─── COMPLETE FRAME ────────────────────────────────────
module cubix_frame() {
    difference() {
        frame_shell();
        all_port_bores();
        access_hatch();
        shaft_feedthrough();
        corner_bracket_holes();
        viewport_holes();
    }
}

// ─── RENDER ────────────────────────────────────────────
color("Silver", 0.5)
    cubix_frame();

%color("crimson")
    cylinder(h=FRAME_OUTER*1.2, d=1, center=true);

// ─── ECHO GEOMETRY ────────────────────────────────────
echo(str("Frame outer:      ", FRAME_OUTER,       " mm"));
echo(str("Frame wall:       ", FRAME_WALL,        " mm"));
echo(str("Frame inner clear:", FRAME_INNER,       " mm"));
echo(str("Port bores:       12 × Ø", PORT_D,      " mm"));
echo(str("Hatch:            ", HATCH_SIZE, "×",   HATCH_SIZE, " mm"));
