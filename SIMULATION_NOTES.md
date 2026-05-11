# Simulation Notes — CUBIX-ICODED v0.4.0

## Model Assumptions

### Magnetic Field
- Halbach array approximated as 4-harmonic Fourier expansion
- Air-gap attenuation: `B(k) = Br * exp(-k * gap / r)` per harmonic
- 4:1 field asymmetry (inner:outer) per Halbach geometry
- Mutual coupling between clusters neglected in 1-D model
- 2-D flux grid uses superposition of 60 point dipoles

### Electromagnetic Torque
- Back-EMF: `e = N * B_avg * A_coil * ω`
- Coil impedance: `Z = √(R² + (ωL)²)`, R = 2.5 Ω, L = 1.2 mH per coil
- 9 harvesting coils in parallel, 3 impulse coils driven
- Bearing friction modeled as: `T_f = 0.015 + 1.8e-8 * ω^1.8`

### Structural
- Rotating disk hoop stress (Lamé): `σ = ρ·ω²·r²·(3+ν)/4`
- PEEK-CF properties: ρ = 1420 kg/m³, E = 12 GPa, σ_y = 180 MPa, ν = 0.38
- SmCo magnet: ρ = 8400 kg/m³, 25×10×5 mm
- Bond shear limit: Loctite EA9492 @ 28 MPa, contact area 250 mm²

## Known Simplifications

1. **3-D flux coupling** between adjacent clusters ignored
2. **Cogging torque** not included (requires FEM)
3. **Temperature effects** on SmCo Br not modeled (Br drops ~0.035%/°C)
4. **Bismuth core** diamagnetic shielding treated as boundary condition only
5. **Vacuum chamber** effects (Phase 3) not included in current model

## Recommended FEM Validation

- FEMM 4.2 (2D magnetostatics) — free, Windows
- OpenFOAM + electromagnetics module (3D)
- Ansys Maxwell (full 3D, commercial)

## Key Results (Phase 1 target: 3,000 RPM)

| Parameter | Value |
|---|---|
| Peak flux density (inner Halbach) | ~2.1 T |
| Mean flux density at stator | ~0.42 T |
| Back-EMF per harvest coil @ 3k RPM | ~0.9 V |
| Total harvest EMF @ 3k RPM | ~8.1 V |
| Net torque @ 3k RPM | ~0.18 N·m |
| Rotor hoop stress @ 3k RPM | ~0.08 MPa (SF >> 100) |
| Centrifugal force per magnet @ 3k RPM | ~0.09 N |
