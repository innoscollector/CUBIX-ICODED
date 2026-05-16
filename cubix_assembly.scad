// =====================================================
// cubix_assembly.scad — Full System Assembly Preview
// CUBIX-ICODED | Phase 0 Geometry
// =====================================================
// Renders all components concentrically.
// Toggle show_* flags to isolate individual parts.
// Use explode > 0 for exploded view.
// =====================================================

include <cubix_params.scad>
use <cubix_rotor.scad>
use <cubix_stator.scad>
use <cubix_frame.scad>
use <cubix_core.scad>

// ─── ASSEMBLY OPTIONS ─────────────────────────────────
show_frame   = true;
show_stator  = true;
show_rotor   = true;
show_core    = true;
show_shaft   = true;
explode      = 0;     // 0 = assembled, 1 = fully exploded

// ─── FULL ASSEMBLY ────────────────────────────────────
module cubix_full_assembly() {
    if (show_frame)
        color("Silver", 0.12)
        translate([0, 0, explode * 220])
            cubix_frame();

    if (show_stator)
        color("ForestGreen", 0.3)
        translate([0, 0, explode * 110])
            cubix_stator();

    if (show_rotor)
        color("SteelBlue", 0.75)
            cubix_rotor();

    if (show_core)
        cubix_core();

    if (show_shaft)
        color("Gray", 0.6)
        difference() {
            cylinder(h=310, d=SHAFT_D, center=true, $fn=36);
            cylinder(h=312, d=SHAFT_D-8, center=true, $fn=36);
        }

    // Coordinate cross (ghost)
    %color("crimson") {
        cylinder(h=420, d=0.6, center=true);
        rotate([90,0,0]) cylinder(h=420, d=0.6, center=true);
        rotate([0,90,0]) cylinder(h=420, d=0.6, center=true);
    }
}

cubix_full_assembly();

// ─── CROSS-SECTION VIEW ───────────────────────────────
// Uncomment block below to see internal cross-section:
/*
intersection() {
    cubix_full_assembly();
    translate([0, -250, -250])
        cube([500, 500, 500]);
}
*/
