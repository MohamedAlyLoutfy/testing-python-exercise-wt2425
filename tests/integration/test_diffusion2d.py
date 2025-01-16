"""
Tests for functionality checks in class SolveDiffusion2D
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Integration test for functions initialize_domain and initialize_physical_parameters
    """
    solver = SolveDiffusion2D()
    
    solver.initialize_domain(w=5.0, h=5.0, dx=1.0, dy=1.0)
    solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)
    
    dx2, dy2 = solver.dx ** 2, solver.dy ** 2
    expected_dt = dx2 * dy2 / (2 * solver.D * (dx2 + dy2))
    
    assert solver.dt == expected_dt, f"Expected dt={expected_dt}, got {solver.dt}"



def test_set_initial_condition():
    """
    Integration test for set_initial_condition
    """
    solver = SolveDiffusion2D()
    
    solver.initialize_domain(w=10.0, h=10.0, dx=1.0, dy=1.0)
    solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)
    
    u = solver.set_initial_condition()
    
    r, cx, cy = 2, 5, 5
    T_hot = 700.0
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 < r ** 2:
                assert u[i, j] == T_hot, f"Expected T_hot at ({i}, {j}), got {u[i, j]}"

    T_cold = 300.0
    for i in range(solver.nx):
        for j in range(solver.ny):
            p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
            if p2 >= r ** 2:
                assert u[i, j] == T_cold, f"Expected T_cold at ({i}, {j}), got {u[i, j]}"

