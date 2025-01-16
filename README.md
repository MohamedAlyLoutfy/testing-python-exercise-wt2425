# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log
pytest tests/unit/test_diffusion2d_functions.py
==================================================== test session starts =====================================================
platform win32 -- Python 3.9.0, pytest-7.4.4, pluggy-1.3.0
rootdir: C:\MSC3\SImulation\testing-python-exercise-wt2425
plugins: anyio-4.3.0
collected 3 items

tests\unit\test_diffusion2d_functions.py F..                                                                            [100%]

========================================================== FAILURES ==========================================================
___________________________________________________ test_initialize_domain ___________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w, h, dx, dy = 5.0, 10.0, 1.0, 0.5
        expected_nx = int(w / dx)
        expected_ny = int(h / dy)

        solver.initialize_domain(w=w, h=h, dx=dx, dy=dy)

>       assert solver.nx == expected_nx, f"Expected nx={expected_nx}, got {solver.nx}"
E       AssertionError: Expected nx=5, got 10
E       assert 10 == 5
E        +  where 10 = <diffusion2d.SolveDiffusion2D object at 0x000001DD12739760>.nx

tests\unit\test_diffusion2d_functions.py:20: AssertionError
================================================== short test summary info =================================================== 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - AssertionError: Expected nx=5, got 10
================================================ 1 failed, 2 passed in 0.84s ================================================= 


### unittest log
 python -m unittest tests/unit/test_diffusion2d_functions.py
Fdt = 0.0625
.dt = 0.0625
.
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D)
Check function SolveDiffusion2D.initialize_domain.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\MSC3\SImulation\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 24, in test_initialize_domain
    self.assertEqual(self.solver.nx, expected_nx, f"Expected nx={expected_nx}, got {self.solver.nx}")
AssertionError: 10 != 5 : Expected nx=5, got 10

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)
PS C:\MSC3\SImulation\testing-python-exercise-wt2425> 


### Integration test log
pytest tests/integration/test_diffusion2d.py
==================================================== test session starts =====================================================
platform win32 -- Python 3.9.0, pytest-7.4.4, pluggy-1.3.0
rootdir: C:\MSC3\SImulation\testing-python-exercise-wt2425
plugins: anyio-4.3.0
collected 2 items

tests\integration\test_diffusion2d.py F.                                                                                [100%]

========================================================== FAILURES ==========================================================
____________________________________________ test_initialize_physical_parameters _____________________________________________

    def test_initialize_physical_parameters():
        """
        Integration test for functions initialize_domain and initialize_physical_parameters
        """
        solver = SolveDiffusion2D()

        # Set up the domain and physical parameters
        solver.initialize_domain(w=5.0, h=5.0, dx=1.0, dy=1.0)
        solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)

        # Expected dt calculation
        dx2, dy2 = solver.dx ** 2, solver.dy ** 2
        expected_dt = dx2 * dy2 / (2 * solver.D * (dx2 + dy2))

>       assert solver.dt == expected_dt, f"Expected dt={expected_dt}, got {solver.dt}"
E       AssertionError: Expected dt=0.0625, got 0.03125
E       assert 0.03125 == 0.0625
E        +  where 0.03125 = <diffusion2d.SolveDiffusion2D object at 0x0000029C0264A6D0>.dt

tests\integration\test_diffusion2d.py:23: AssertionError
---------------------------------------------------- Captured stdout call ---------------------------------------------------- 
dt = 0.03125
================================================== short test summary info =================================================== 
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - AssertionError: Expected dt=0.0625, got 0.03125
================================================ 1 failed, 1 passed in 0.80s ================================================= 


pytest tests/integration/test_diffusion2d.py
==================================================== test session starts =====================================================
platform win32 -- Python 3.9.0, pytest-7.4.4, pluggy-1.3.0
rootdir: C:\MSC3\SImulation\testing-python-exercise-wt2425
plugins: anyio-4.3.0
collected 2 items

tests\integration\test_diffusion2d.py .F                                                                                [100%]

========================================================== FAILURES ==========================================================
_________________________________________________ test_set_initial_condition _________________________________________________

    def test_set_initial_condition():
        """
        Integration test for set_initial_condition
        """
        solver = SolveDiffusion2D()

        # Set up the domain and physical parameters
        solver.initialize_domain(w=10.0, h=10.0, dx=1.0, dy=1.0)
        solver.initialize_physical_parameters(d=4.0, T_cold=300.0, T_hot=700.0)

        u = solver.set_initial_condition()

        # Check that points inside the circle are set to T_hot
        r, cx, cy = 2, 5, 5
        T_hot = 700.0
        for i in range(solver.nx):
            for j in range(solver.ny):
                p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
                if p2 < r ** 2:
>                   assert u[i, j] == T_hot, f"Expected T_hot at ({i}, {j}), got {u[i, j]}"
E                   AssertionError: Expected T_hot at (4, 4), got 300.0
E                   assert 300.0 == 700.0

tests\integration\test_diffusion2d.py:46: AssertionError
---------------------------------------------------- Captured stdout call ---------------------------------------------------- 
dt = 0.0625
================================================== short test summary info =================================================== 
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError: Expected T_hot at (4, 4), got 300.0 
================================================ 1 failed, 1 passed in 0.80s ================================================= 
PS C:\MSC3\SImulation\testing-python-exercise-wt2425> 


## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
