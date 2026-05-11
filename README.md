
CUBIX-ICODED

**Experimental Electromechanical Geometry Platform**

**Author:** Bojan Sebastian Andrei (Cluj-Napoca, Romania)

## Overview
CUBIX-ICODED is an open-source experimental electromechanical research platform focused on asymmetric electromagnetic geometry, modular rotor/stator architectures, and high-speed nested polyhedral systems. 

The project combines:
- Icosahedral rotor geometry (vertex-centric magnetic distribution)
- Dodecahedral stator topology (phase-offset harvesting)
- Halbach-inspired 4:1 magnetic star clusters
- Pentagonal Bipyramidal diamagnetic core
- Parametric CAD/CNC construction
- Vacuum/plasma-compatible structural design

CUBIX-ICODED is presented as an evolving engineering research platform intended for CAD prototyping, electromagnetic experimentation, rotational dynamics analysis, flux distribution studies, and collaborative open-source development.

## Development Philosophy
**observe → measure → refine → repeat**

The system is not presented as a finalized technology, but as a continuously evolving experimental architecture. All energetic, electromagnetic, or plasma-related hypotheses remain under active investigation and require independent measurement and validation.

## Core Architecture & Geometric Stack
The system is organized concentrically into 5 functional layers:
1. **External Frame:** Cubic Titanium Grade 5 structure (330 mm, 8 mm wall thickness).
2. **Shielding:** Rhombic Triacontahedron for EMF Cusp confinement and flux stabilization.
3. **Stator:** Dodecahedral system for coil nesting.
4. **Rotor:** Icosahedral matrix for high-speed dynamic flux projection.
5. **Central Core:** Pentagonal Bipyramidal structure utilizing high-purity Bismuth (diamagnetic) for field stabilization without inducing Foucault currents on the central axis.

## Technical Specifications

### Rotor Architecture (Icosahedron)
- **Geometry:** 20 equilateral triangles, 115.34 mm edge length.
- **Assembly Angle:** 20.905° bevel (chamfer) on edges for structural interlocking.
- **Materials:** PEEK-CF / composite experimental variants (3 mm to 8 mm variable thickness).
- **Magnetic Distribution:** 60 SmCo magnets (25x10x5 mm) organized in 12 clusters. Each cluster forms a pentagonal star at the icosahedron's vertices, forcing a 4:1 asymmetric Halbach projection.

### Stator & Phase-Offset Harvesting (Dodecahedron)
- **Ports:** 12 total (3 impulse gates for excitation, 9 harvesting gates).
- **Angular Offset:** The architecture imposes a strict **31.71°** angular offset between the harvesting gates and the primary magnetic vectors.
- **Objective:** Investigating phase displacement behavior, asymmetric field interaction, and reactive drag reduction (Back-EMF management).
- **Topology:** The 9 harvesting ports are grouped into 3 triplets for distributed load balancing and capacitive recovery experimentation.

### Mechanical & Operational Parameters
- **Air Gap:** Target radial clearance of **0.30 mm**.
- **Precession Tolerance:** Experimental induced precession target of **0.02 mm**.
- **Assembly Precision:** Gate positioning tolerance of **±0.005 mm**; angular positioning of **±0.01°**.
- **Operational Environment:** Designed for controlled vacuum environments (10^-6 Torr) with optional inert Argon/Krypton plasma injection to manipulate ionic conductivity.
- **Rotational Target:** Phase 1 prototyping at 2,000 - 3,000 RPM; final structural validation at 25,000 RPM.

## Roadmap

**Phase 1**
- Rotor geometry validation
- Modular assembly system (dowel pin integration)
- Precision balancing
- Structural integrity testing

**Phase 2**
- Coil system implementation (Litz wire, bifilar winding concepts)
- Sensor integration & RPM monitoring
- Vibration mapping

**Phase 3**
- Vacuum testing
- Magnetic flux analysis
- Thermal behavior evaluation
- Dynamic phase experimentation

**Phase 4**
- Prototype refinement
- Iterative optimization
- Community collaboration & independent replication attempts

## Important Disclaimer
CUBIX-ICODED is an experimental research project. Any performance hypotheses, theoretical interpretations, or unconventional electromagnetic concepts discussed within the project are exploratory and subject to ongoing testing, validation, and independent verification. The repository is intended primarily for engineering experimentation and geometric research.

## Repository Structure
```text
CUBIX-ICODED/
├── README.md
├── ROADMAP.md
├── BOM.md
├── LICENSE
├── cubix_visualizer.py
├── CAD/
│   ├── Fusion360/
│   └── Renders/
├── Simulations/
├── Experimental-Logs/
├── Coil-Configs/
├── Docs/
└── Prototype/


## Closing Statement
CUBIX-ICODED represents a long-term experimental exploration into advanced electromechanical geometries, asymmetric field interaction, and modular engineering systems. The objective is not to claim finalized answers, but to build, test, measure, and evolve an open experimental platform through continuous iteration.
