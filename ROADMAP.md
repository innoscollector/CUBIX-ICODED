# CUBIX-ICODED — Roadmap

**Author:** Bojan Sebastian Andrei (Cluj-Napoca, Romania)  
**Repo:** https://github.com/innoscollector/CUBIX-ICODED  
**Philosophy:** observe → measure → refine → repeat

---

## Phase 1 — Geometry Validation & Structural Assembly
**Status:** 🟡 In Progress

- [ ] Rotor icosahedral geometry — CAD finalization (Fusion 360)
- [ ] 20.905° bevel edge validation on PEEK-CF panels
- [ ] Modular assembly system — dowel pin integration
- [ ] SmCo magnet cluster layout — Halbach star verification (Gauss meter)
- [ ] Precision dynamic balancing (< 0.02 mm precession)
- [ ] Structural integrity testing at 2,000–3,000 RPM
- [ ] Titanium frame CNC fabrication
- [x] Digital geometry visualizer (`cubix_visualizer.py`)
- [x] Bill of Materials v0.3 (`BOM.md`)

---

## Phase 2 — Coil System & Instrumentation
**Status:** ⚪ Planned

- [ ] Coil bobbin CNC fabrication (PEEK/PTFE, Ø30 mm)
- [ ] Litz wire winding — impulse gates (I1–I3), ~80 turns
- [ ] Bifilar winding — harvesting gates (H1–H9), ~120 turns
- [ ] 31.71° phase offset verification — stator gate alignment
- [ ] Hall effect sensor integration (3× at 120° spacing)
- [ ] RPM monitoring system (optical tachometer + Hall)
- [ ] Vibration mapping — axial + radial (ADXL345)
- [ ] Coil resistance & inductance baseline measurement
- [ ] Capacitor recovery bank (9× 100µF film caps)

---

## Phase 3 — Vacuum Testing & Electromagnetic Analysis
**Status:** ⚪ Planned

- [ ] Vacuum pump stack installation (Pfeiffer rotary + turbo)
- [ ] Vacuum chamber seal verification (10⁻⁶ Torr target)
- [ ] Bearing performance at reduced pressure
- [ ] Magnetic flux distribution mapping (Gauss meter sweep)
- [ ] Thermal behavior evaluation — K-type thermocouple array
- [ ] Back-EMF waveform capture — oscilloscope analysis
- [ ] Phase displacement behavior documentation
- [ ] Argon/Krypton plasma injection (ionic conductivity experiment)

---

## Phase 4 — Refinement & Open Collaboration
**Status:** ⚪ Future

- [ ] Prototype iteration based on Phase 3 data
- [ ] CAD model release (Fusion 360 / STEP / STL)
- [ ] Simulation data publication (Simulations/)
- [ ] Independent replication guide (Docs/)
- [ ] Community collaboration — open issue tracker
- [ ] Iterative coil geometry optimization
- [ ] Paper / technical report draft

---

## Revision Log

| Version | Date    | Notes                              |
|---------|---------|------------------------------------|
| v0.1    | 2026-05 | Initial roadmap draft              |
