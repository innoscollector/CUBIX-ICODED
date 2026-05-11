# Hardware Assembly Guide — CUBIX-ICODED

## Safety

> ⚠️  SmCo N52 magnets at 25×10×5 mm produce ~0.6 T surface field.
> Keep away from pacemakers, magnetic media, and ferrous tools.
> Use PEEK or non-magnetic jigs for assembly.

## Phase 1 Build Sequence

### 1. Frame (Ti Grade 5)
1. Machine outer ring to 330 mm OD, 4 mm wall
2. Drill 20 M3 mounting holes on dodecahedron vertex positions
3. Anodize or passivate surfaces

### 2. Bismuth Core
1. Cast Bi 99.99% into 56 mm diameter sphere (3D-printed mold)
2. Machine to final diameter after casting
3. Press-fit or epoxy into PEEK center hub

### 3. Rotor (PEEK-CF panels)
1. CNC-mill 20 triangular panels from PEEK-CF sheet (edge 115.34 mm, bevel 20.905°)
2. Route Halbach magnet pockets: 5 pockets per panel, 4:1 cluster ratio
3. Press SmCo magnets into pockets — verify orientation with Hall probe
4. Bond with Loctite EA9492 (cure 24 h at RT, post-cure 2 h @ 80°C)
5. Dynamic balance rotor assembly (target: < 0.5 g·mm residual imbalance)

### 4. Stator (Dodecahedral frame)
1. Machine 12 port faces with Litz wire channels
2. Wind 3 impulse coils (80 turns, 0.5 mm Litz) at 0°, 120°, 240°
3. Wind 9 harvest coils (120 turns, 0.35 mm Litz) with 31.71° offset
4. Pot coils in thermally conductive epoxy

### 5. Mu-metal EMF Shield
1. Cut 12 panels of Mu-metal (t=0.5mm) to dodecahedral pattern
2. Anneal at 1100°C in H₂ atmosphere after forming
3. Install between stator and Ti frame

### 6. Bearing & Final Assembly
1. Press Si₃N₄ ceramic bearings (bore to match shaft)
2. Set air gap to 0.30 mm using feeler gauge + laser alignment
3. Torque all fasteners to spec (M3: 0.5 N·m, M5: 2.5 N·m)

## Air Gap Setting Procedure
1. Install rotor without magnets first
2. Measure runout with dial indicator (target: < 0.05 mm TIR)
3. Adjust bearing preload
4. Install magnets cluster by cluster, re-check gap after each cluster

## Initial Spin Test (Phase 1)
- Start at 100 RPM, monitor vibration and temperature
- Step up 500 RPM every 2 minutes
- Record back-EMF per coil at each step
- Target 3,000 RPM with all coils producing expected waveforms
