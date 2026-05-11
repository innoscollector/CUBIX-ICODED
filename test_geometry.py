"""
CUBIX-ICODED — Geometry Validation Tests
Run: python -m pytest tests/ -v
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import numpy as np
import pytest
from cubix_sim import (
    PHI, EDGE_MM, OFFSET_DEG,
    icosahedron_vertices, icosahedron_faces, dodecahedron_vertices,
    halbach_field_1d, torque_vs_rpm, rotor_stress,
)


class TestIcosahedron:
    def setup_method(self):
        self.verts = icosahedron_vertices(EDGE_MM / 2)
        self.faces = icosahedron_faces(self.verts)

    def test_vertex_count(self):
        assert len(self.verts) == 12

    def test_face_count(self):
        assert len(self.faces) == 20

    def test_all_edges_equal(self):
        edge_len = np.linalg.norm(self.verts[0] - self.verts[1])
        tol = edge_len * 0.01
        for f in self.faces:
            i, j, k = f
            assert abs(np.linalg.norm(self.verts[i] - self.verts[j]) - edge_len) < tol
            assert abs(np.linalg.norm(self.verts[j] - self.verts[k]) - edge_len) < tol
            assert abs(np.linalg.norm(self.verts[i] - self.verts[k]) - edge_len) < tol

    def test_centroid_at_origin(self):
        centroid = self.verts.mean(axis=0)
        assert np.allclose(centroid, 0, atol=1e-10)

    def test_circumradius(self):
        # All vertices at same distance from origin
        radii = np.linalg.norm(self.verts, axis=1)
        assert np.allclose(radii, radii[0], rtol=1e-6)


class TestDodecahedron:
    def setup_method(self):
        self.verts = dodecahedron_vertices(EDGE_MM / 2 * 1.3)

    def test_vertex_count(self):
        assert len(self.verts) == 20

    def test_centroid_at_origin(self):
        centroid = self.verts.mean(axis=0)
        assert np.allclose(centroid, 0, atol=1e-10)


class TestMagneticField:
    def test_halbach_asymmetry(self):
        theta = np.linspace(0, 2 * np.pi, 360)
        B_in, B_out = halbach_field_1d(theta)
        # Inner field should be stronger (4:1)
        assert np.mean(np.abs(B_in)) > np.mean(np.abs(B_out))
        ratio = np.mean(np.abs(B_in)) / np.mean(np.abs(B_out))
        assert 3.5 < ratio < 4.5

    def test_field_periodicity(self):
        theta = np.linspace(0, 2 * np.pi, 720, endpoint=False)
        B_in, _ = halbach_field_1d(theta)
        # Field should be periodic (first ≈ last)
        assert abs(B_in[0] - B_in[-1]) < 0.01


class TestDynamics:
    def test_torque_increases_with_rpm(self):
        rpm, T_net, T_fric, T_em, EMF, eff = torque_vs_rpm()
        # Electromagnetic torque should increase initially
        mid = len(rpm) // 3
        assert T_em[mid] > T_em[1]

    def test_emf_proportional_to_rpm(self):
        rpm, _, _, _, EMF, _ = torque_vs_rpm()
        # At low RPM, EMF ∝ ω (before impedance dominates)
        idx_1k = np.argmin(np.abs(rpm - 1000))
        idx_2k = np.argmin(np.abs(rpm - 2000))
        ratio = EMF[idx_2k] / EMF[idx_1k]
        assert 1.8 < ratio < 2.2

    def test_efficiency_bounded(self):
        _, _, _, _, _, eff = torque_vs_rpm()
        assert np.all(eff >= 0)
        assert np.all(eff <= 1)


class TestStructural:
    def test_stress_increases_with_rpm(self):
        rpm, sigma, F_cent, SF = rotor_stress()
        assert sigma[-1] > sigma[0]

    def test_safety_factor_at_low_rpm(self):
        rpm, sigma, F_cent, SF = rotor_stress(np.array([1000.0]))
        # At 1k RPM, safety factor should be very high
        assert SF[0] > 50

    def test_safety_critical_at_high_rpm(self):
        rpm, sigma, F_cent, SF = rotor_stress(np.array([25000.0]))
        # At 25k RPM, SF should still be > 1 (design intent)
        assert SF[0] > 1.0
