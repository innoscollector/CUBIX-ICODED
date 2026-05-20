⚙️ Engineering Updates & Technical Constraints
To ensure structural integrity and operational efficiency at high RPMs, the following parameters have been strictly defined:
Mechanical Reinforcement:
Pins/Fasteners: Upgraded from initial M3/M4 standard to Ø6 mm × 12 mm high-tensile custom pins. This upgrade is mandatory to withstand the calculated centrifugal forces of 39.5 kN occurring at peak operating speeds.
Structural Tolerance: All internal alignment pins must maintain a tolerance of < 0.1 mm to prevent harmonic vibration coupling.
Dynamic Thermal & Kinetic Compensation:
Air Gap Tuning: Adjusted the air gap from 0.30 mm to 0.50 mm. This precise margin is critical to compensate for the calculated 0.316 mm elastic deformation of the PEEK-CF rotor structure under maximum load, preventing contact with the stator.
Thermal Expansion: The 0.2–0.5 mm thermal clearance (as specified in the technical PDF) is now a hard requirement to prevent internal stress during plasma-state stabilization.
Operational RPM Limits (Safety Protocol):
33 cm Scale (Full Assembly): Software-locked at 25,000 RPM via ICODED firmware to ensure safe operation within the tensile limits of the Grade 5 Titanium housing.
Sub-scale/Micro-models (≤10 cm): High-velocity threshold of up to 100,000 RPM is permissible only for validation models using ultra-light composite rotors, provided they pass a strict dynamic balancing test (unbalance threshold < 0.01 g).
Geometric Flux Alignment:
Critical Offset: The system maintains a constant 31.71° phase offset, derived from the Golden Ratio symmetry (\arccos(1/\phi^2)), specifically engineered to bypass Lenz's Law braking effects through temporal induction delay.
