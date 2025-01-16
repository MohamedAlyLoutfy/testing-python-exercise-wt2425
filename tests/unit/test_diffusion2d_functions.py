"""
Tests for functions in class SolveDiffusion2D
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from diffusion2d import SolveDiffusion2D


import unittest

class TestDiffusion2D(unittest.TestCase):
    def setUp(self):
        """Common setup for all tests."""
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """Check function SolveDiffusion2D.initialize_domain."""
        w, h, dx, dy = 5.0, 10.0, 1.0, 0.5
        expected_nx = int(w / dx)
        expected_ny = int(h / dy)

        self.solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

        self.assertEqual(self.solver.nx, expected_nx, f"Expected nx={expected_nx}, got {self.solver.nx}")
        self.assertEqual(self.solver.ny, expected_ny, f"Expected ny={expected_ny}, got {self.solver.ny}")

    def test_initialize_physical_parameters(self):
        """Check function SolveDiffusion2D.initialize_physical_parameters."""
        self.solver.initialize_domain(w=5.0, h=5.0, dx=1.0, dy=1.0)

        d = 4.0
        T_cold = 300.0
        T_hot = 700.0
        dx2, dy2 = self.solver.dx * self.solver.dx, self.solver.dy * self.solver.dy
        expected_dt = dx2 * dy2 / (2 * d * (dx2 + dy2))

        self.solver.initialize_physical_parameters(d=d, T_cold=T_cold, T_hot=T_hot)

        self.assertEqual(self.solver.D, d, f"Expected D={d}, got {self.solver.D}")
        self.assertEqual(self.solver.T_cold, T_cold, f"Expected T_cold={T_cold}, got {self.solver.T_cold}")
        self.assertEqual(self.solver.T_hot, T_hot, f"Expected T_hot={T_hot}, got {self.solver.T_hot}")
        self.assertAlmostEqual(self.solver.dt, expected_dt, places=6, msg=f"Expected dt={expected_dt}, got {self.solver.dt}")

    def test_set_initial_condition(self):
        """Check function SolveDiffusion2D.set_initial_condition."""
        self.solver.initialize_domain(w=10.0, h=10.0, dx=1.0, dy=1.0)
        self.solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)

        u = self.solver.set_initial_condition()

        r, cx, cy = 2, 5, 5
        T_hot = 700.0
        for i in range(self.solver.nx):
            for j in range(self.solver.ny):
                p2 = (i * self.solver.dx - cx) ** 2 + (j * self.solver.dy - cy) ** 2
                if p2 < r ** 2:
                    self.assertEqual(u[i, j], T_hot, f"Expected T_hot at ({i}, {j}), got {u[i, j]}")

        T_cold = 300.0
        for i in range(self.solver.nx):
            for j in range(self.solver.ny):
                p2 = (i * self.solver.dx - cx) ** 2 + (j * self.solver.dy - cy) ** 2
                if p2 >= r ** 2:
                    self.assertEqual(u[i, j], T_cold, f"Expected T_cold at ({i}, {j}), got {u[i, j]}")


