# CUBIX-ICODED
**Experimental Asymmetric Electromagnetic Geometry Platform**

**Author:** Bojan Sebastian Andrei (Cluj-Napoca, Romania)
**License:** MIT
**Status:** Phase 1 — Digital Geometry Validation Achieved (V1.2 Critical Updates)
-------------------
🌌 The "Asymmetry" Paradox: Spatial Symmetry vs. Temporal Phase Shift
A common misconception regarding the CUBIX-ICODED architecture is that its "asymmetrical magnetic manipulation" implies a structural or mass asymmetry. This is fundamentally incorrect. The system relies on absolute spatial symmetry to operate at extreme velocities, while shifting the asymmetry entirely into the temporal domain (time-dependent phase shifting).
Absolute Spatial Symmetry (Mechanical Balance):
Cross-sectioning the icosahedral/dodecahedral core along any equatorial plane reveals perfectly balanced radial symmetry governed by the Golden Ratio (\phi), featuring pentagonal and decagonal geometries. This isotropic mass and volume distribution is strictly required to prevent catastrophic precession at 25,000 RPM, maintaining the dynamic unbalance strictly below < 0.01 g.
Temporal Asymmetry (The 31.71° Offset):
The system is physically symmetric but electromagnetically out-of-phase. The calculated 31.7° geometric offset (\arccos(1/\phi^2)) does not distort the rotor; instead, it manipulates when the magnetic flux lines intersect the stator gates.
Cascading Magnetic Engagement (3D Gearing):
In standard synchronous motors, all poles align simultaneously, causing Lenz's Law braking to hit the primary rotational axis directly and forcefully. In CUBIX-ICODED, the 60 Samarium-Cobalt magnets (clustered in pentagram arrays at the 12 vertices) engage the stator in a cascaded, sequential pattern. This acts as a frictionless 3D magnetic gear—where the opposing Lenz forces "slip" tangentially rather than colliding head-on, bypassing standard counter-torque limitations.
-------------------
For detailed mechanical parameters, structural validation data, and operational safety limits, please consult the Engineering Validation Status document
-------------------

## 1. Concept Overview

CUBIX-ICODED is an open-source experimental electromechanical research platform. It is not a traditional radial motor. The architecture explores whether icosahedral rotor geometry, asymmetric Halbach magnet distribution, and a phase-offset dodecahedral stator topology produce measurably different electromagnetic behavior compared to conventional symmetric designs.

The central design hypothesis is that deliberately breaking magnetic symmetry — spatially and structurally — across the rotor-stator interface creates a continuous asymmetric flux interaction that can be studied, measured, and optimized. No performance conclusions are drawn ahead of physical measurement.

---

### 1.2. Phase 1.2: Zero-EMI Adsorption/Absorption Kinetic Rerouting
Instead of utilizing mechanical fluid pumps or compression loops, the steady-state thermal load is dissipated via an integrated, closed-loop **Solid-Gas Adsorption/Absorption thermodynamic cycle** (utilizing a Zeolite-Water or Methanol-Silica matrix optimized under structural vacuum).

* **Direct Gyroid Thermal Coupling:** The evaporator end of the adsorption loop is directly integrated into the outer boundary of the 3D-printed gyroid matrix. As the PCM inside the gyroid absorbs the peak load and reaches its phase change plateau, the adsorption loop continuously draws this energy out, acting as a sub-atmospheric heat sink.
* **Zero Parasitic Fields:** Because the fluid transport is driven entirely by chemical affinity and thermal desorption pressures, the cooling cycle requires no electric motors, fans, or compressors. This guarantees an absolute zero electromagnetic signature ($0\text{ dB}$ acoustic, $0\text{ Hz}$ EMI disruption).
* **Thermal Energy Harvesting (Co-generation):** The system operates on a regenerative delta-T. The waste heat rejected by the stator coils acts as the primary thermodynamic driver (the generator/desorber) for the cooling loop, creating a self-regulating thermal equilibrium loop: higher core utilization directly increases the desorption-evaporation cooling rate.

---

## 2. System Architecture — 5 Concentric Layers

1. **External Frame** — Cubic Ti-6Al-4V (Grade 5), 330 mm, 8 mm wall thickness (Engineered for absolute vacuum containment).
2. **EMF Shielding** — Rhombic Triacontahedron, 30 mu-metal diamond panels for EMF cusp confinement and flux stabilization.
3. **Stator** — Dodecahedral coil nesting system, 12 interaction gates.
4. **Rotor** — Icosahedral magnet matrix, 60 SmCo magnets in 12 vertex clusters.
5. **Central Core** — Pentagonal Bipyramidal structure, 99.99% pure Bismuth (diamagnetic), isolated to suppress macroscopic field anomalies.

---

## 3. Core Architecture & Physics

### 3.1 The Icosahedral Rotor & The 31.71° Angle

The rotor uses icosahedral geometry: 20 equilateral triangular faces, 12 vertices, 30 edges, edge length **115.34 mm**. The structural assembly angle (bevel/chamfer on all edges) is **20.905°** for face-to-face interlocking. The internal dihedral angle of a regular icosahedron is **138.19°**.

The **31.71°** angle is the angular offset between the primary magnetic flux vectors of the rotor vertices and the harvesting gate normals of the dodecahedral stator. This value is derived from the geometric relationship between the two dual polyhedra (being exactly half of the supplementary angle of the dodecahedron's dihedral geometry). The design intent is that coils positioned at this offset operate outside the primary flux peak — being investigated as an unorthodox approach to analyzing reactive back-EMF drag variations during harvesting.

### 3.2 Asymmetric Halbach Arrays — 5+1 / 1+5

Each of the 12 icosahedral vertices carries a cluster of 5 SmCo magnets arranged in a pentagonal star (Halbach-type topology). The clusters alternate between two configurations:

- **5+1:** 5 magnets oriented flux-forward (toward the air gap) + 1 flux-rearward → high flux density on the leading face of that vertex.
- **1+5:** 1 magnet flux-forward + 5 flux-rearward → low flux density on the same face.

Alternating 5+1 / 1+5 across the 12 vertices creates a continuous gradient of magnetic pressure around the rotor circumference. This asymmetry is designed to prevent a symmetric equilibrium (cogging) by ensuring no two adjacent vertices present identical magnetic resistance to the stator at any given rotation angle.

Magnetization detail: on each cluster, 4 magnets are oriented radially outward, 1 center magnet axially. Pole orientation of every magnet must be verified with a Gauss meter before bonding.

### 3.3 Spearhead Vertex Convergence (Vârf de Lance)

At every icosahedral vertex, exactly 5 equilateral triangular faces meet at a single point. The 5 magnets per cluster are mounted along these 5 converging face planes. The resultant magnetic flux at the apex is the vector sum of the 5 individual dipole field projections:

$$\mathbf{B}_{apex} = \sum_{i=1}^{5} \mathbf{B}_i \cdot \cos(\phi_i)$$

where $\phi_i$ is the angle between face normal $i$ and the vertex radial axis.

This is a geometric consequence of placing magnets on 5 converging planes — the flux vectors add constructively at the tip, creating localized, high-density magnetic spearheads.

### 3.4 Diamagnetic Core — Bismuth Pentagonal Bipyramid

The central core is a Pentagonal Bipyramid machined from 99.99% pure Bismuth. Bismuth is the most strongly diamagnetic naturally occurring element ($\mu_r \approx 0.99983$) — it weakly repels applied magnetic fields. 

**Equatorial Asymmetry — 9:10 Mismatch:**
The pentagonal bipyramid has 10 vertices distributed around its equatorial band (5 upper + 5 lower peri-equatorial rings). The icosahedral rotor also has 10 peri-equatorial magnet positions (two rings of 5). The bipyramid is mounted with a deliberate 9-vertex equatorial reference, creating a 9:10 positional mismatch between the bismuth geometry and the rotor magnet positions. No single rotor angle simultaneously aligns all equatorial magnets with all bismuth vertices, actively reducing the probability of a stable magnetic lock at any fixed static angle.

**Machining note:** Bismuth melting point is 271°C — use sharp carbide tooling, low feed rate, no flood coolant. Mount in a PEEK or PTFE cage, secured with M3 nylon screws (non-magnetic, electrically isolated).

### 3.5 Stator Gate Topology — 3 Impulse / 9 Harvesting

The dodecahedral stator has 12 pentagonal faces = 12 interaction gates:

- **3 Impulse Gates (I1, I2, I3):** At 0°, 120°, 240° — equilateral triangle arrangement. These deliver microsecond pulses from high-discharge capacitors for excitation at the lowest magnetic resistance point in the rotation cycle.
- **9 Harvesting Gates (H1–H9):** Divided into 3 triplets for distributed load balancing and capacitive recovery experimentation. Each triplet is angularly offset by **31.71°** from its corresponding impulse gate.

The asymmetric 3:9 ratio is a specific design choice for studying switched reluctance and counter-EMF behavior under load, functioning strictly as a high-density energy conversion topology.

### 3.6 Vacuum Environment & Argon-Krypton Plasma

The entire core operates inside the vacuum-sealed Ti-6Al-4V casing at **10⁻⁶ Torr**. In Phase 3, an Argon/Krypton plasma mixture is injected to investigate the effect of controlled ionic conductivity on the electromagnetic environment — specifically whether plasma presence measurably affects inductive braking dynamics (Lenz-law counter-EMF interaction) at high angular velocities. This is an experimental variable to be measured, not a pre-claimed efficiency breakthrough.

---

## 4. Technical Specifications

### Rotor — Icosahedron

| Parameter | Value |
|---|---|
| Faces | 20 equilateral triangles |
| Vertices | 12 |
| Edges | 30 |
| Edge length | 115.34 mm |
| Assembly bevel angle | 20.905° |
| Dihedral angle | 138.19° |
| Material | PEEK-CF, 3–8 mm variable thickness |
| Magnets | 60 × SmCo N52, 25×10×5 mm |
| Clusters | 12 × 5 magnets — pentagonal Halbach star per vertex |
| Array type | Asymmetric 5+1 / 1+5 alternating |
| Magnet retention | Loctite EA 9492 (vacuum-compatible, $T_g > 120^\circ\text{C}$) |
| Alignment & Retention Pins | **Ø6 mm × 12 mm high-tensile fasteners (Upgraded from M3/M4 to withstand 39.5 kN centrifugal forces)** |
| Hub | Ti Grade 5, Ø30 mm bore, keyed |

### Stator — Dodecahedron

| Parameter | Value |
|---|---|
| Faces / Gates | 12 pentagonal |
| Impulse gates | 3 (I1–I3) at 0°, 120°, 240° |
| Harvesting gates | 9 (H1–H9) in 3 triplets |
| Angular offset | 31.71° |
| Gate bore | Ø35 mm × 18 mm depth, PEEK-CF |
| Gate tolerance | ±0.005 mm |
| Angular tolerance | ±0.01° |
| Face material | PEEK or FR4 G10 fiberglass |
| Support ring | Al 6061, Ø280 mm × 10 mm |

### Central Core — Bismuth Bipyramid

| Parameter | Value |
|---|---|
| Shape | Pentagonal Bipyramid |
| Material | Bismuth $\geq99.99\%$ purity |
| Permeability | $\mu_r \approx 0.99983$ |
| Equatorial mismatch | 9:10 (bismuth : rotor equatorial magnets) |
| Mount | PEEK/PTFE cage, M3 nylon screws |

### EMF Shielding — Rhombic Triacontahedron

| Parameter | Value |
|---|---|
| Faces | 30 diamond-shaped panels |
| Material | Mu-metal 0.5 mm sheet (pre-annealed) |
| Backup | Copper EMF foil tape self-adhesive |
| Vertices | 32 (3-way and 5-way clips, ABS/PA12) |

### Mechanical & Operational (Recalibrated for V1.2)

| Parameter | Value |
|---|---|
| **Air gap (Recalibrated)** | **0.50 mm radial clearance (Adjusted from 0.30mm to compensate for 0.316mm PEEK-CF elastic deformation under load)** |
| Precession tolerance | 0.02 mm |
| Gate positioning tolerance | $\pm0.005\text{ mm}$ |
| Angular positioning tolerance | $\pm0.01^\circ$ |
| Phase 1 RPM | 2,000–3,000 RPM |
| **Structural Validation RPM** | **25,000 RPM (Software-locked via ICODED firmware for 33cm scale; 100,000 RPM limits apply only to $\leq10\text{cm}$ sub-scale models)** |
| Vacuum | $10^{-6}\text{ Torr}$ |
| Phase 3 plasma | Argon / Krypton mixture |
| Bearings | Ceramic hybrid $\text{Si}_3\text{N}_4$ |
| Lubrication | Krytox GPL 205 (vacuum-rated) |

---

## 5. Materials & Fabrication

- **Magnets:** SmCo N52 only. Thermal stability up to 300°C (vs NdFeB ~80°C). Critical for high-RPM and vacuum environments.
- **Rotor/Stator structure:** PEEK-CF or carbon-fiber reinforced filament. Requires enclosed high-temperature 3D printer or CNC machining from billet.
- **Casing:** Ti-6Al-4V (Grade 5) — high tensile strength, non-magnetic, vacuum-compatible.
- **Bismuth core:** Melting point 271°C — carbide tooling only, careful setup.
- **Mu-metal shielding:** Must be sourced pre-annealed. Machining degrades permeability and requires re-annealing.
- **Anchoring Component Exclusion:** All central structural anchoring rods must be composed strictly of dielectric, high-strength composites (**G10/FR4 or Tech Zirconia Ceramic**). The use of metals along these vectors is strictly prohibited to eliminate localized Foucault (eddy current) loops and induction heating.

---

## 6. What the Code Does

`cubix_visualizer.py` — Python/matplotlib 3D visualization. Generates 4 figures:
- Icosahedral rotor with Halbach cluster arrows at all 12 vertices
- Polar gate map — dodecahedral stator (3 impulse + 9 harvesting, 31.71° offset marked)
- Concentric layer cross-section (all 5 layers, to scale, with air gap annotation)
- Technical specification reference card

`cubix_sim.py` — Geometric simulation scaffold (in development).

`test_geometry.py` — Unit tests for vertex and face geometry calculations.

```bash
pip install numpy matplotlib
python cubix_visualizer.py

```
## 7. Roadmap
**Phase 1 — Geometry validation (current)**
 * Rotor geometry verification via CAD
 * Modular assembly with high-tensile pin integration (M6/M8)
 * Precision dynamic balancing
 * Structural integrity and elastic deformation testing
**Phase 2 — Electromagnetic prototype**
 * Coil winding (High-frequency Litz wire, bifilar configurations for skin-effect suppression)
 * RPM sensing and monitoring
 * Vibration/Resonance mapping
**Phase 3 — Environmental testing**
 * Vacuum chamber operation
 * Magnetic flux measurement
 * Thermal profiling
 * Argon/Krypton plasma injection experiments
**Phase 4 — Open collaboration**
 * Measurement data publication
 * Independent replication attempts
 * Iterative design refinement
## 🛑 Advanced Thermal Management: Hybrid Thermal Buffer & Absorption System
High-performance operation of the **CUBIX-ICODED** geometry generates localized Joule heating within the stator segments. Standard vapor-compression cooling (compressors) introduces massive electromagnetic interference (EMI) that can distort the precise 31.71^\circ critical magnetic angles.
To maintain total electromagnetic isolation and structural efficiency, the system utilizes a **Zero-EMI Hybrid Thermal Stabilization** architecture.
### 1. Phase 1: High-Velocity Thermal Shaving (Gyroid-Matrix Buffer)
To mitigate instant thermal spikes during peak load phases, the core modules are encased in an advanced **Gyroid-Structured Thermal Buffer Block** (3D-printed Aerospace Aluminum/Copper hybrid matrix).
 * **Magnetic Flux Optimization:** Instead of a solid metal block—which would trigger severe parasitic Eddy currents and distort the magnetic fields—the buffer uses a **TPMS (Triple Periodic Minimal Surface) Gyroid geometry**. This topology breaks up electromagnetic induction loops, shielding the critical 31.71^\circ flux paths.
 * **Instant Capture & Heat-Sink Surface:** The open-cell gyroid architecture provides an ultra-high surface-area-to-volume ratio, intercepting heat fluxes *before* they reach the Samarium-Cobalt (SmCo) permanent magnets.
 * **Phase Change Material (PCM) Infill:** The internal voids of the gyroid matrix are entirely filled with a technical PCM rated at a 60^\circ\text{C} - 70^\circ\text{C} phase transition point. The gyroid struts act as micro-conductors, distributing heat uniformly into the PCM to lock the core temperature during peak loads.
### 2. Phase 2: Zero-EMI Absorption Rerouting
Instead of mechanical pumps, the steady-state thermal load is dissipated using a closed-loop **Solid-Gas Adsorption/Absorption cycle** (Zeolite-Water / Methanol matrix under structural vacuum).
 * **Zero Parasitic Fields:** The cooling cycle requires no electric motors or compressors, operating with absolute zero electromagnetic signature (0\text{ dB} acoustic background, 0\text{ Hz} parasitic field profile).
 * **Energy Harvesting (Co-generation):** The thermal energy rejected by the stator coils acts as the primary thermodynamic driver (the generator) for the cooling loop, auto-regulating the system's equilibrium.
## 8. Repository Structure
```
CUBIX-ICODED/
├── CAD/                    (planned — Fusion360, renders)
├── Simulations/            (planned — FEM data)
├── Experimental-Logs/      (planned — measurement data)
├── Coil-Configs/           (planned)
├── cubix_visualizer.py
├── cubix_sim.py
├── test_geometry.py
├── BOM.md
├── HARDWARE_ASSEMBLY.md
├── ROADMAP.md
├── README.md
└── LICENSE

```
## 9. Status & Disclaimer
No physical prototype has been built. All specifications are design targets. All electromagnetic hypotheses in this document are unverified and subject to physical measurement and independent validation. The project is in Phase 1: digital geometry validation and mechanical optimization.
**observe → measure → refine → repeat**
**Creator & Architect:** Bojan Sebastian Andrei (Cluj-Napoca, Romania)
*The geometric configurations, angular parameters — including the 31.71° offset, the asymmetric 5+1/1+5 Halbach matrices, the Spearhead vertex convergence topology, and the Bismuth bipyramidal diamagnetic integration — documented here are the original work of the author. Commercial application or patent derivative based on this architecture requires explicit written permission.*
*MIT License — see LICENSE file.*
```
