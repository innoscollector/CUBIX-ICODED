# Changelog — CUBIX-ICODED

## [v0.4.0] — 2025 (current)
### Added
- Full physics simulation engine (`sim/cubix_sim.py`)
- CAD geometry export to JSON (`cad/CUBIX_CAD_data.json`)
- Magnetic flux density field simulation (Halbach 4:1)
- Electromagnetic torque & Back-EMF curves
- Structural integrity analysis (PEEK-CF hoop stress)
- Gate EMF waveforms (3 impulse + 9 harvesting, 31.71° offset)
- `requirements.txt` for reproducible installs
- `docs/` folder with simulation notes and hardware assembly guide
- `tests/` folder with geometry validation

## [v0.3.0]
### Added
- `BOM.md` — full bill of materials with cost estimates (€1,700–€2,900 Phase 1)
- `cubix_visualizer.py` — 4-panel matplotlib visualizer

## [v0.2.0]
### Added
- Initial geometry definition (icosahedron rotor + dodecahedron stator)
- Edge length 115.34 mm, bevel 20.905°, phase offset 31.71°

## [v0.1.0]
### Added
- Project scaffold, README, LICENSE (MIT)
