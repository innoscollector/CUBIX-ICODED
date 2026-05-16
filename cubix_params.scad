// =====================================================
// cubix_params.scad — CUBIX-ICODED Shared Parameters
// Author: Bojan Sebastian Andrei (Cluj-Napoca, Romania)
// Status: Phase 0 — Digital Geometry Validation
// Rev: v0.3-pre-prototype
// =====================================================

// ─── MATHEMATICAL CONSTANTS ──────────────────────────
PHI = (1 + sqrt(5)) / 2;           // Golden ratio ≈ 1.618033...

// ─── ROTOR — ICOSAHEDRAL MATRIX ──────────────────────
ROTOR_EDGE       = 115.34;         // Panel edge length (mm)
ROTOR_WALL       = 5.0;            // Panel wall thickness — PEEK-CF (mm)
ROTOR_BEVEL      = 20.905;         // Edge chamfer angle (degrees)

// ─── MAGNETIC SYSTEM ─────────────────────────────────
MAG_L            = 25.0;           // Magnet length (mm)
MAG_W            = 10.0;           // Magnet width (mm)
MAG_D            = 5.0;            // Magnet depth into panel (mm)
MAG_CLEAR        = 0.15;           // Pocket assembly clearance (mm)
MAG_PER_CLUSTER  = 5;              // SmCo magnets per vertex cluster
NUM_CLUSTERS     = 12;             // = number of icosahedron vertices

// ─── SHAFT & BEARINGS ────────────────────────────────
SHAFT_D          = 30.0;           // Shaft diameter (mm)
SHAFT_TOL        = 0.02;           // Bore H7 tolerance (mm)
BEARING_OD       = 62.0;           // 6006 series bearing OD (mm)
BEARING_W        = 16.0;           // Bearing width (mm)
KEYWAY_W         = 8.0;            // Keyway width (mm)
KEYWAY_H         = 4.0;            // Keyway depth (mm)

// ─── AIR GAP ─────────────────────────────────────────
AIR_GAP          = 0.30;           // Radial rotor-stator clearance (mm)
PRECESSION_TOL   = 0.02;           // Max allowed precession (mm)

// ─── STATOR — DODECAHEDRAL SYSTEM ────────────────────
// Inradius of stator = rotor circumradius + air gap
// Rotor circumradius = ROTOR_EDGE × 0.9511 (icosahedron geometry)
// Dodecahedron: inradius = edge × 1.1135
ROTOR_CIRCUM     = ROTOR_EDGE * 0.9511;            // ≈ 109.7 mm
STATOR_INRAD     = ROTOR_CIRCUM + AIR_GAP;         // ≈ 110.0 mm
STATOR_EDGE      = STATOR_INRAD / 1.1135;          // ≈  98.8 mm
STATOR_WALL      = 6.0;            // Shell thickness — PEEK (mm)
COIL_BORE_D      = 35.0;           // Coil gate bore diameter (mm)
COIL_BORE_DEPTH  = 18.0;           // Coil gate bore depth (mm)
STATOR_OFFSET    = 31.71;          // Phase offset angle (degrees)
STATOR_RING_D    = 280.0;          // Support ring outer diameter (mm)
STATOR_RING_T    = 10.0;           // Support ring thickness (mm)

// ─── GATE ASSIGNMENT ─────────────────────────────────
// Face indices 0-2  → Impulse gates  I1, I2, I3
// Face indices 3-11 → Harvesting gates H1-H9
NUM_IMPULSE      = 3;
NUM_HARVEST      = 9;

// ─── EMF SHIELDING — RHOMBIC TRIACONTAHEDRON ─────────
SHIELD_PANEL_A   = 52.0;           // Panel long edge ≈ 50 mm (approx)

// ─── EXTERNAL FRAME — CUBIC Ti STRUCTURE ─────────────
FRAME_OUTER      = 330.0;          // Outer cube dimension (mm)
FRAME_WALL       = 8.0;            // Wall thickness — Ti Grade 5 (mm)
FRAME_INNER      = FRAME_OUTER - 2*FRAME_WALL;     // 314.0 mm
PORT_D           = 45.0;           // Frame port bore diameter (mm)
HATCH_SIZE       = 80.0;           // Access hatch side (mm)
M6_BORE          = 6.5;            // M6 clearance bore (mm)

// ─── CENTRAL CORE — PENTAGONAL BIPYRAMIDAL ───────────
CORE_R           = 28.0;           // Equatorial radius — Bismuth (mm)
CORE_H           = 30.0;           // Half-height of bipyramid (mm)
CORE_WALL        = 4.0;            // PEEK cage wall thickness (mm)

// ─── RENDER QUALITY ──────────────────────────────────
$fn  = 72;                         // Default circle resolution
$eps = 0.01;                       // Boolean overlap epsilon
