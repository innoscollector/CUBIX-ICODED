# CUBIX-ICODED — Bill of Materials (BOM)
**Revision:** v0.3-pre-prototype  
**Author:** Bojan Sebastian Andrei (Cluj-Napoca, Romania)  
**Status:** 🟡 Planning / Pre-Fabrication  
**Last updated:** 2026-05

> ⚠️ This BOM covers the Phase 1 prototype assembly. Quantities and specifications are subject to revision as CAD models are finalized. All tolerances referenced are target design values.

---

## Table of Contents

1. [External Frame](#1-external-frame--cubic-titanium-structure)
2. [EMF Shielding Layer](#2-emf-shielding-layer--rhombic-triacontahedron)
3. [Stator — Dodecahedral System](#3-stator--dodecahedral-system)
4. [Rotor — Icosahedral Matrix](#4-rotor--icosahedral-matrix)
5. [Central Core — Pentagonal Bipyramidal](#5-central-core--pentagonal-bipyramidal)
6. [Coil System](#6-coil-system)
7. [Bearings & Shaft](#7-bearings--shaft)
8. [Fasteners & Structural Hardware](#8-fasteners--structural-hardware)
9. [Sensors & Instrumentation](#9-sensors--instrumentation)
10. [Vacuum & Environmental Equipment](#10-vacuum--environmental-equipment)
11. [Tools & Fabrication Equipment](#11-tools--fabrication-equipment)
12. [Cost Estimate Summary](#12-cost-estimate-summary)

---

## 1. External Frame — Cubic Titanium Structure

| # | Component | Spec | Qty | Unit | Material | Notes |
|---|-----------|------|-----|------|----------|-------|
| 1.1 | Titanium plate — frame walls | 330×330×8 mm | 6 | pcs | Ti Grade 5 (Ti-6Al-4V) | CNC milled; 6 faces of cubic enclosure |
| 1.2 | Corner connectors / brackets | Custom L-bracket, M6 thread | 12 | pcs | Ti Grade 5 | Precision-drilled; ±0.01 mm alignment |
| 1.3 | Mounting bosses for stator ports | Ø12 mm, M6 female thread | 12 | pcs | Ti Grade 5 | One per dodecahedral gate |
| 1.4 | Access hatch (vacuum seal) | 80×80 mm, O-ring groove | 1 | pcs | Ti Grade 5 + Viton O-ring | For instrumentation lead-through |

**Supplier options:** Alibaba (Ti plate), local CNC service (Cluj/Brașov), or online: [titaniumjoe.com](https://titaniumjoe.com), [metals4u.co.uk](https://metals4u.co.uk)  
**Estimated cost:** ~€600–900 (raw material + basic CNC)

---

## 2. EMF Shielding Layer — Rhombic Triacontahedron

| # | Component | Spec | Qty | Unit | Material | Notes |
|---|-----------|------|-----|------|----------|-------|
| 2.1 | Rhombic panels | 30 diamond-shaped faces, ~50 mm edge | 30 | pcs | Mu-metal 0.5 mm sheet | High-permeability alloy for EMF cusp confinement |
| 2.2 | Panel edge joiners | Custom 3-way / 5-way vertex clips | 32 | pcs | ABS or Nylon PA12 | 3D-printed; non-magnetic |
| 2.3 | Inner liner tape | 50 mm wide, self-adhesive | 2 | rolls | Copper EMF foil | Faraday layer backup |

**Notes:** Mu-metal requires annealing after machining. Source pre-annealed sheets.  
**Supplier options:** [magnetic-shield.com](https://www.magnetic-shield.com), [lessemf.com](https://www.lessemf.com)  
**Estimated cost:** ~€180–280

---

## 3. Stator — Dodecahedral System

| # | Component | Spec | Qty | Unit | Material | Notes |
|---|-----------|------|-----|------|----------|-------|
| 3.1 | Pentagonal face panels | Regular pentagon, ~90 mm edge | 12 | pcs | PEEK or FR4 G10 fiberglass | 12 faces; 3 impulse + 9 harvesting gates |
| 3.2 | Coil gate inserts | Ø35 mm bore, 18 mm depth | 12 | pcs | PEEK-CF | CNC bored; ±0.005 mm on diameter |
| 3.3 | Vertex joining rods | M4 threaded, 40 mm length | 20 | pcs | Titanium or G10 rods | Non-magnetic; 20 vertices of dodecahedron |
| 3.4 | Phase label markers | Laser-engraved or anodized | 12 | pcs | Aluminum 6061 | I1–I3 (impulse), H1–H9 (harvest) |
| 3.5 | Stator support ring | Ø280 mm × 10 mm annular ring | 1 | pcs | Aluminum 6061 | Centering mount inside Ti frame |
| 3.6 | Angular offset reference plate | 31.71° precision-engraved dial | 1 | pcs | Stainless 316L | Assembly alignment reference |

**Estimated cost:** ~€120–200 (materials); CNC cost separate

---

## 4. Rotor — Icosahedral Matrix

| # | Component | Spec | Qty | Unit | Material | Notes |
|---|-----------|------|-----|------|----------|-------|
| 4.1 | Triangular rotor panels | Equilateral triangle, 115.34 mm edge | 20 | pcs | PEEK-CF 5 mm thick | 20 faces; 20.905° bevel on all edges |
| 4.2 | Edge bevel tolerance | 20.905° chamfer | — | — | — | CNC only; hand-filing introduces imbalance |
| 4.3 | SmCo permanent magnets | 25×10×5 mm, N52 grade | 60 | pcs | SmCo (Samarium Cobalt) | 12 clusters × 5 magnets; Halbach-star arrangement |
| 4.4 | Magnet retention epoxy | High-temp, low-outgassing | 1 | tube | Loctite EA 9492 or similar | Vacuum-compatible; Tg > 120°C |
| 4.5 | Dowel pin alignment kit | Ø3 mm × 10 mm hardened | 60 | pcs | Stainless 316L | Edge-to-edge interlocking; modular assembly |
| 4.6 | Rotor hub / central shaft collar | Ø30 mm bore, keyed | 1 | pcs | Titanium Grade 5 | Precision-turned; 0.02 mm precession tolerance |
| 4.7 | Dynamic balancing weights | M2 set screws, various | 1 | set | Stainless 316L | Post-assembly precision balancing |

**Magnet notes:**  
- SmCo selected over NdFeB for thermal stability (operating temp up to 300°C vs 80°C for NdFeB)  
- Each cluster forms a pentagonal Halbach star; pole orientation must be verified with Gauss meter before bonding  
- Magnetization direction: radially outward on 4 magnets, axially on 1 center magnet per cluster

**Supplier options:** [supermagnete.de](https://www.supermagnete.de), [kjmagnetics.com](https://www.kjmagnetics.com), [first4magnets.com](https://www.first4magnets.com)  
**Estimated cost:** ~€200–350 (magnets ~€120, PEEK-CF panels ~€140)

---

## 5. Central Core — Pentagonal Bipyramidal

| # | Component | Spec | Qty | Unit | Material | Notes |
|---|-----------|------|-----|------|----------|-------|
| 5.1 | Bismuth core billet | ~60 mm height, ~30 mm diameter | 1 | pcs | Bismuth ≥99.99% purity | Diamagnetic; μr ≈ 0.99983; no Foucault currents |
| 5.2 | Bismuth machining note | — | — | — | — | Low melting point (271°C); use sharp carbide tools, no coolant flood |
| 5.3 | Core support cage | Pentagonal bipyramid skeleton | 1 | pcs | PEEK or PTFE | Non-conductive; holds Bismuth at rotor center |
| 5.4 | Core-to-hub mount | M3 nylon screws × 5 | 5 | pcs | Nylon PA6 | Non-magnetic; electrically isolated |

**Bismuth notes:**  
- Bismuth is the most naturally diamagnetic element; repels magnetic fields without superconducting temp requirements  
- Must be protected from rotor impact — fragile under dynamic stress above ~15,000 RPM  
- Alternative for Phase 1 testing: PTFE (Teflon) dummy core — same geometry, zero risk of fracture

**Supplier options:** [rotometals.com](https://www.rotometals.com), [metallium.com](https://www.metallium.com)  
**Estimated cost:** ~€40–80 (99.99% Bismuth ~500g block)

---

## 6. Coil System

| # | Component | Spec | Qty | Unit | Material | Notes |
|---|-----------|------|-----|------|----------|-------|
| 6.1 | Litz wire — primary | AWG 26, 100-strand, 2m sections | 12 | pcs | Copper Litz | High-frequency loss reduction; one reel per gate |
| 6.2 | Bifilar winding sections | AWG 28, bifilar pair | 9 | pcs | Copper Litz | Harvesting coils only (H1–H9) |
| 6.3 | Coil bobbins | Ø30 mm × 18 mm | 12 | pcs | PEEK or PTFE | CNC-turned; fits gate insert bore |
| 6.4 | Coil varnish / potting | Vacuum-compatible, low-outgassing | 1 | can | MG Chemicals 4228 or Humiseal | Applied under vacuum for void-free potting |
| 6.5 | Capacitor bank (recovery) | 100 µF / 100V, low-ESR | 9 | pcs | Film capacitor (WIMA or Panasonic) | One per harvesting gate for capacitive recovery |
| 6.6 | Terminal block connectors | 2-pole, rated 20A | 12 | pcs | Brass / PCB-mount | Phase grouping: 3 triplets + 3 impulse lines |

**Winding notes:**  
- Impulse gate coils: ~80 turns, bifilar option to be tested  
- Harvesting gate coils: ~120 turns, optimized for 31.71° phase offset geometry  
- All coils wound before installation; resistance measured before mounting

**Estimated cost:** ~€80–140

---

## 7. Bearings & Shaft

| # | Component | Spec | Qty | Unit | Material | Notes |
|---|-----------|------|-----|------|----------|-------|
| 7.1 | Angular contact bearing (upper) | 6006-2RS, Ø30mm bore | 1 | pcs | Ceramic hybrid (Si3N4 balls) | Non-magnetic; vacuum-rated lubricant |
| 7.2 | Angular contact bearing (lower) | 6006-2RS, Ø30mm bore | 1 | pcs | Ceramic hybrid | Paired pre-load arrangement |
| 7.3 | Main rotor shaft | Ø30mm × 200mm, keyway 8×4 mm | 1 | pcs | Titanium Grade 5 | Turned; ground to h6 tolerance |
| 7.4 | Shaft collar — upper | Ø40 mm, Ø30 bore | 1 | pcs | Aluminum 6061 | Rotor axial lock |
| 7.5 | Bearing lubricant | Vacuum-rated grease | 1 | tube | Krytox GPL 205 or Fomblin | Outgassing < 10⁻⁹ Torr·L/s |
| 7.6 | Shaft seal (if partial vacuum) | FKM / Viton lip seal, Ø30mm | 2 | pcs | Viton | For moderate vacuum; omit for high-vac |

**Notes:** Ceramic hybrid bearings chosen for: non-magnetic, higher speed rating, lower thermal expansion, no electrical conductivity (eliminates electrical arcing in plasma environment)

**Supplier options:** [boca-bearings.com](https://www.boca-bearings.com) (ceramic), [vxb.com](https://www.vxb.com)  
**Estimated cost:** ~€120–200

---

## 8. Fasteners & Structural Hardware

| # | Component | Spec | Qty | Unit | Material | Notes |
|---|-----------|------|-----|------|----------|-------|
| 8.1 | Frame assembly bolts | M6 × 20mm socket head | 48 | pcs | Titanium Grade 5 | Non-magnetic; 8 per frame face |
| 8.2 | Stator mounting bolts | M4 × 12mm | 24 | pcs | A4 Stainless or Ti | Stator-to-support ring |
| 8.3 | Internal alignment pins | Ø3 mm × 15 mm | 40 | pcs | Hardened stainless 316L | Precision Ø tolerance h6 |
| 8.4 | Thread-locking compound | Medium strength | 2 | tubes | Loctite 243 | Vibration-proof; removable |
| 8.5 | Vacuum-compatible sealant | For port sealing | 1 | tube | Apiezon Q or Torr Seal | All vacuum-side joints |

**Estimated cost:** ~€60–100

---

## 9. Sensors & Instrumentation

| # | Component | Spec | Qty | Unit | Notes |
|---|-----------|------|-----|------|-------|
| 9.1 | Hall effect sensor (RPM) | A1302 or SS495A, linear | 3 | pcs | Mounted at stator; 120° spacing |
| 9.2 | Gauss / Tesla meter | Range: 0–3 T, ±1% accuracy | 1 | pcs | For magnet cluster verification pre-assembly |
| 9.3 | Vibration accelerometer | ADXL345 or piezo | 2 | pcs | Axial + radial mounting points |
| 9.4 | Thermocouples — K type | Range: -50 to 400°C | 4 | pcs | Bearing housings + coil temperature |
| 9.5 | Data logger / DAQ | 8-channel, USB, 10 kHz sample rate | 1 | pcs | Arduino Mega + ADS1115 or NI DAQ |
| 9.6 | Oscilloscope | ≥100 MHz, 4-channel | 1 | pcs | Coil waveform analysis (Rigol DS1054Z is adequate) |
| 9.7 | Optical tachometer | Laser reflective, 0–99,999 RPM | 1 | pcs | RPM cross-check; window port in frame |

**Estimated cost:** ~€200–350

---

## 10. Vacuum & Environmental Equipment

| # | Component | Spec | Qty | Unit | Notes |
|---|-----------|------|-----|------|-------|
| 10.1 | Rotary vane vacuum pump | 2-stage, 0.1 mTorr base pressure | 1 | pcs | Pfeiffer Duo 3 or equivalent; ~€600–900 used |
| 10.2 | Turbomolecular pump | Reach 10⁻⁶ Torr | 1 | pcs | Pfeiffer TMH 071 or similar; ~€1,500–2,500 used |
| 10.3 | Vacuum gauges | Pirani + ion gauge combo | 1 | set | Full range: atmosphere to 10⁻⁷ Torr |
| 10.4 | KF25 / KF40 vacuum fittings | Flanges, elbows, tees | 1 | set | All stainless 304 |
| 10.5 | Inert gas system (Phase 3) | Argon / Krypton MFC + regulator | 1 | set | For plasma injection experiments |
| 10.6 | Viewport window | Borosilicate, KF40 flange | 2 | pcs | Optical access; laser tachometer pass-through |
| 10.7 | Feedthroughs — electrical | 12-pin, KF40 flange, 20A rated | 2 | pcs | Coil connections through vacuum wall |

**Notes:** Phase 1 can run at atmospheric pressure. Vacuum equipment required from Phase 3 onward.  
**Estimated cost (Phase 3):** ~€2,000–4,000 (pump stack; significant used market available)

---

## 11. Tools & Fabrication Equipment

| # | Tool | Minimum Spec | Notes |
|---|------|-------------|-------|
| 11.1 | CNC milling machine | ±0.01 mm positioning | Outsource for Ti Grade 5; in-house for PEEK |
| 11.2 | Metal 3D printer (future) | DMLS or SLM, Ti-capable | Target acquisition; for frame prototyping |
| 11.3 | Precision lathe | Ø capability > 40 mm | Shaft and bearing housing turning |
| 11.4 | Digital micrometer set | 0.001 mm resolution | Air gap and tolerance verification |
| 11.5 | CMM / precision height gauge | 0.001 mm | Rotor face flatness verification |
| 11.6 | Dynamic balancing machine | Supports Ø > 150 mm | Phase 1 balancing to < 0.02 mm precession |
| 11.7 | Torque wrench | 0.5–20 Nm, calibrated | Fastener spec compliance |
| 11.8 | Coil winding jig | Custom, per bobbin spec | DIY-fabricated from aluminum |

---

## 12. Cost Estimate Summary

| Section | Component Group | Phase 1 Est. (€) | Phase 3 Est. (€) |
|---------|----------------|-----------------|-----------------|
| 1 | External Frame (Ti) | 600–900 | 600–900 |
| 2 | EMF Shielding Layer | 180–280 | 180–280 |
| 3 | Stator System | 120–200 | 120–200 |
| 4 | Rotor — Icosahedral | 200–350 | 200–350 |
| 5 | Central Core (Bi) | 40–80 | 40–80 |
| 6 | Coil System | 80–140 | 80–140 |
| 7 | Bearings & Shaft | 120–200 | 120–200 |
| 8 | Fasteners & Hardware | 60–100 | 60–100 |
| 9 | Sensors & Instrumentation | 200–350 | 200–350 |
| 10 | Vacuum Equipment | — | 2,000–4,000 |
| 11 | Tooling (one-time) | 100–300 | 100–300 |
| **TOTAL** | | **~€1,700–2,900** | **~€3,700–6,900** |

> 💡 **Phase 1 can realistically begin under €2,000** if CNC work is outsourced locally and vacuum equipment is deferred.  
> Used pump stacks from eBay / LabX / Surplus equipment resellers can cut Phase 3 vacuum costs by 50–70%.

---

## Revision Log

| Version | Date | Changes |
|---------|------|---------|
| v0.1 | 2025-xx | Initial component identification |
| v0.2 | 2026-04 | Added coil system, sensor list, vacuum stack |
| v0.3 | 2026-05 | Full BOM draft with cost estimates and supplier notes |

---

*This BOM is maintained alongside the CUBIX-ICODED CAD repository. Component specifications will be revised as 3D models are finalized. All cost estimates are approximate and subject to regional supplier availability.*
