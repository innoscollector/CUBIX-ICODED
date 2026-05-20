# Module 2: Rotor Dynamics, Geometry & Kinetic Constraints

## 1. Geometric Topology & Magnetic Mass
The moving core of the system utilizes a perfect regular icosahedron geometry to ensure isotropic structural integrity and multi-directional flux projection.
* **Core Geometry:** Regular Icosahedron (12 vertices, 20 equilateral faces).
* **Material:** High-performance Carbon Fiber-reinforced Polyether ether ketone (PEEK-CF) for the primary structural matrix. Metallic components are strictly prohibited in the rotor body to completely eliminate parastic Eddy currents (Curenți Foucault).
* **Magnetic Matrix Array (Halbach Configuration):**
  * **Total Magnets:** 60 Samarium-Cobalt (SmCo) permanent magnets.
  * **Distribution:** Clustered in sets of 5 at each of the 12 vertices, forming a pentagram-star configuration.
  * **Flux Profile:** Each 5-magnet vertex cluster compresses and accelerates the magnetic field lines outward, generating a high-density, multi-polar spherical vortex.
  * **Internal Repulsion:** Internal mounting slots must withstand a violent self-repulsion force of **200–500 N per magnet** inherent to the Halbach positioning.

## 2. Kinetic Stress & High-Tensile Fastening
Operating at hyper-velocities transforms minimal structural tolerances into massive kinetic loads. The fastening architecture is engineered for high shear resistance:
* **Fastener Specifications:** Custom high-tensile pins measuring **Ø6 mm × 12 mm** are integrated at all critical joint interfaces.
* **Load Containment:** The pinning system is rated to safely absorb a peak radial centrifugal force of **39.5 kN** generated at maximum operational velocity.
* **Alignment Tolerances:** Mechanical mounting slots require a strict tolerance threshold of **< 0.1 mm** to prevent structural micro-shifting during acceleration phases.

## 3. Deformations, Air-Gap Tuning & Balancing
To preserve the integrity of the electromagnetic gap without causing mechanical failure, the system balances expansion tolerances against flux degradation:
* **Elastic Deformation:** Under maximum centrifugal load, the PEEK-CF rotor matrix undergoes a calculated radial elastic expansion of **0.316 mm**.
* **Air-Gap Calibration:** To absorb this physical expansion, the clearance between the rotor and stator is locked at **0.50 mm**. This provides a safety margin of approximately 0.184 mm to clear harmonic vibrations, axis precession, and secondary thermal expansion.
* **Dynamic Balancing Threshold:** To prevent destructive structural resonance, the assembled rotor must undergo rigorous multi-plane dynamic balancing. The maximum allowable residual unbalance is strictly capped at **< 0.01 g**.

## 4. Scaled Velocity Operational Thresholds (Firmware Locks)
Velocity limits are hardcoded based on volumetric scale to respect the tensile limits of the Grade 5 Titanium external containment unit:
* **33 cm Full-Scale Model:** Software-locked via ICODED firmware at **25,000 RPM** ($\omega = 2618 \text{ rad/s}$), limiting peripheral acceleration to avoid ballistic fragmentation.
* **Sub-Scale/Micro Models (≤10 cm):** High-velocity thresholds up to **100,000 RPM** are permissible only for ultra-light composite experimental sub-assemblies.
* 
