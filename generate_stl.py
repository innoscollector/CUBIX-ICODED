"""
generate_stl.py — CUBIX-ICODED STL Generator
=============================================
Generates binary STL files for all CUBIX-ICODED components.

Requirements: numpy (already needed by cubix_visualizer.py)
Usage:        python generate_stl.py
Output:       STL/ folder with one .stl per component

Import into Fusion360: Insert → Insert Mesh → select .stl
Open in OpenSCAD:      File → Open → select .scad (preferred)
"""

import numpy as np
import struct
import os
from pathlib import Path

# ──────────────────────────────────────────────────────
# PARAMETERS (must match cubix_params.scad)
# ──────────────────────────────────────────────────────
PHI          = (1 + np.sqrt(5)) / 2
ROTOR_EDGE   = 115.34
ROTOR_WALL   = 5.0
SHAFT_D      = 30.0
AIR_GAP      = 0.30
STATOR_WALL  = 6.0
FRAME_OUTER  = 330.0
FRAME_WALL   = 8.0
CORE_R       = 28.0
CORE_H       = 30.0
ROTOR_CIRCUM = ROTOR_EDGE * 0.9511
STATOR_INRAD = ROTOR_CIRCUM + AIR_GAP

OUT = Path(__file__).parent / "STL"
OUT.mkdir(exist_ok=True)

# ──────────────────────────────────────────────────────
# BINARY STL WRITER
# ──────────────────────────────────────────────────────
def write_stl(filename, triangles, label="CUBIX"):
    path = OUT / filename
    n = len(triangles)
    with open(path, "wb") as f:
        hdr = f"CUBIX-ICODED {label}".encode()
        f.write(hdr.ljust(80, b"\x00")[:80])
        f.write(struct.pack("<I", n))
        for tri in triangles:
            v0 = np.asarray(tri[0], float)
            v1 = np.asarray(tri[1], float)
            v2 = np.asarray(tri[2], float)
            n_ = np.cross(v1 - v0, v2 - v0)
            ln = np.linalg.norm(n_)
            if ln > 1e-12:
                n_ /= ln
            f.write(struct.pack("<fff", *n_))
            f.write(struct.pack("<fff", *v0))
            f.write(struct.pack("<fff", *v1))
            f.write(struct.pack("<fff", *v2))
            f.write(struct.pack("<H", 0))
    size_kb = path.stat().st_size // 1024
    print(f"  ✓  {filename:<40} {n:>5} triangles  {size_kb} KB")

# ──────────────────────────────────────────────────────
# GEOMETRY HELPERS
# ──────────────────────────────────────────────────────
def fan_tris(verts, face):
    """Fan-triangulate a polygon face."""
    tris = []
    v0 = verts[face[0]]
    for i in range(1, len(face) - 1):
        tris.append((v0, verts[face[i]], verts[face[i + 1]]))
    return tris

def poly_tris(verts, faces):
    tris = []
    for f in faces:
        tris.extend(fan_tris(verts, f))
    return tris

def flip_tris(tris):
    return [(t[0], t[2], t[1]) for t in tris]

def hollow_tris(verts, faces, inner_scale):
    outer = poly_tris(verts, faces)
    iv    = verts * inner_scale
    inner = flip_tris(poly_tris(iv, faces))
    return outer + inner

def cylinder_tris(h, r, n=32, center=True):
    z0, z1 = (-h / 2, h / 2) if center else (0.0, h)
    tris = []
    for i in range(n):
        a0, a1 = 2 * np.pi * i / n, 2 * np.pi * (i + 1) / n
        p00 = [r * np.cos(a0), r * np.sin(a0), z0]
        p10 = [r * np.cos(a1), r * np.sin(a1), z0]
        p01 = [r * np.cos(a0), r * np.sin(a0), z1]
        p11 = [r * np.cos(a1), r * np.sin(a1), z1]
        c0, c1 = [0, 0, z0], [0, 0, z1]
        tris += [(p00, p11, p10), (p00, p01, p11)]   # side
        tris += [(c0, p10, p00)]                      # bottom cap
        tris += [(c1, p01, p11)]                      # top cap
    return tris

def box_tris(sx, sy, sz, center=True):
    hx, hy, hz = sx / 2, sy / 2, sz / 2
    x0, x1 = (-hx, hx) if center else (0, sx)
    y0, y1 = (-hy, hy) if center else (0, sy)
    z0, z1 = (-hz, hz) if center else (0, sz)
    corners = {
        (a, b, c): np.array([x0 if a == 0 else x1,
                              y0 if b == 0 else y1,
                              z0 if c == 0 else z1])
        for a in [0,1] for b in [0,1] for c in [0,1]
    }
    def q(a, b, c, d):
        return [corners[a], corners[b], corners[c], corners[d]]
    quads = [
        q((0,0,0),(0,1,0),(0,1,1),(0,0,1)),  # -X
        q((1,0,0),(1,0,1),(1,1,1),(1,1,0)),  # +X
        q((0,0,0),(0,0,1),(1,0,1),(1,0,0)),  # -Y
        q((0,1,0),(1,1,0),(1,1,1),(0,1,1)),  # +Y
        q((0,0,0),(1,0,0),(1,1,0),(0,1,0)),  # -Z
        q((0,0,1),(0,1,1),(1,1,1),(1,0,1)),  # +Z
    ]
    tris = []
    for q_ in quads:
        tris += [(q_[0], q_[1], q_[2]), (q_[0], q_[2], q_[3])]
    return tris

# ──────────────────────────────────────────────────────
# ICOSAHEDRON
# ──────────────────────────────────────────────────────
def ico_verts(edge=ROTOR_EDGE):
    s = edge / 2
    return np.array([
        [0,  1,  PHI], [0, -1,  PHI], [0,  1, -PHI], [0, -1, -PHI],
        [1,  PHI, 0],  [-1, PHI, 0],  [1, -PHI, 0],  [-1, -PHI, 0],
        [PHI, 0,  1],  [-PHI, 0,  1], [PHI, 0, -1],  [-PHI, 0, -1]
    ]) * s

def ico_faces():
    return [
        [0,1,8],[0,8,4],[0,4,5],[0,5,9],[0,9,1],
        [3,10,2],[3,6,10],[3,7,6],[3,11,7],[3,2,11],
        [1,6,8],[6,10,8],[8,10,4],[10,2,4],[4,2,5],
        [2,11,5],[5,11,9],[11,7,9],[9,7,1],[1,7,6],
    ]

# ──────────────────────────────────────────────────────
# DODECAHEDRON
# ──────────────────────────────────────────────────────
def dode_raw_verts():
    p, ip = PHI, 1 / PHI
    return np.array([
        [ 1, 1, 1],[ 1, 1,-1],[ 1,-1, 1],[ 1,-1,-1],
        [-1, 1, 1],[-1, 1,-1],[-1,-1, 1],[-1,-1,-1],
        [ 0, ip, p],[ 0,-ip, p],[ 0, ip,-p],[ 0,-ip,-p],
        [ ip, p, 0],[-ip, p, 0],[ ip,-p, 0],[-ip,-p, 0],
        [ p, 0, ip],[ p, 0,-ip],[-p, 0, ip],[-p, 0,-ip],
    ])

def dode_faces():
    return [
        [0,8,4,13,12],[0,12,1,17,16],[0,16,2,9,8],
        [1,10,5,13,12],[1,17,3,11,10],[2,14,3,17,16],
        [2,9,6,15,14],[4,8,9,6,18],[4,18,19,5,13],
        [5,19,7,11,10],[6,15,7,19,18],[3,14,15,7,11],
    ]

def dode_verts(inrad=STATOR_INRAD):
    rv = dode_raw_verts()
    f0 = dode_faces()[0]
    fc = rv[f0].mean(axis=0)
    return rv * (inrad / np.linalg.norm(fc))

# ──────────────────────────────────────────────────────
# BIPYRAMID (core)
# ──────────────────────────────────────────────────────
def bpy_verts(r=CORE_R, h=CORE_H):
    eq = [[r * np.cos(np.radians(72 * i)),
           r * np.sin(np.radians(72 * i)), 0.0] for i in range(5)]
    return eq + [[0, 0, h], [0, 0, -h]]

def bpy_tris(r=CORE_R, h=CORE_H):
    v = bpy_verts(r, h)
    tris = []
    for i in range(5):
        j = (i + 1) % 5
        tris.append((v[i], v[5], v[j]))      # top
        tris.append((v[i], v[j], v[6]))      # bottom
    return tris

# ──────────────────────────────────────────────────────
# GENERATE ALL FILES
# ──────────────────────────────────────────────────────
def gen_rotor():
    v = ico_verts()
    f = ico_faces()
    s = 1 - (2 * ROTOR_WALL / ROTOR_EDGE)
    write_stl("rotor_icosahedron.stl", hollow_tris(v, f, s), "Rotor")

def gen_stator():
    v = dode_verts()
    f = dode_faces()
    s = 1 - (STATOR_WALL / STATOR_INRAD)
    write_stl("stator_dodecahedron.stl", hollow_tris(v, f, s), "Stator")

def gen_frame():
    outer = box_tris(FRAME_OUTER, FRAME_OUTER, FRAME_OUTER)
    inner = flip_tris(box_tris(FRAME_OUTER - 2*FRAME_WALL,
                               FRAME_OUTER - 2*FRAME_WALL,
                               FRAME_OUTER - 2*FRAME_WALL))
    write_stl("frame_cubic.stl", outer + inner, "Frame")

def gen_core():
    write_stl("core_bipyramid_bismuth.stl", bpy_tris(), "Core-Bi")
    # PEEK cage (outer - inner)
    out = bpy_tris(CORE_R + 4, CORE_H + 4)
    inn = flip_tris(bpy_tris(CORE_R + 0.1, CORE_H + 0.1))
    write_stl("core_cage_peek.stl", out + inn, "Core-Cage")

def gen_shaft():
    outer = cylinder_tris(h=310, r=SHAFT_D / 2)
    inner = flip_tris(cylinder_tris(h=312, r=SHAFT_D / 2 - 4))
    write_stl("shaft.stl", outer + inner, "Shaft")

# ──────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    sep = "─" * 52
    print(f"\n{sep}")
    print("  CUBIX-ICODED  —  STL Generator")
    print(f"  Output → {OUT}")
    print(sep)

    gen_rotor()
    gen_stator()
    gen_frame()
    gen_core()
    gen_shaft()

    files = list(OUT.glob("*.stl"))
    total = sum(f.stat().st_size for f in files) // 1024
    print(sep)
    print(f"  {len(files)} files generated   ({total} KB total)")
    print("  Fusion360 : Insert → Insert Mesh → select .stl")
    print("  OpenSCAD  : use .scad files directly (parametric)")
    print(f"{sep}\n")
