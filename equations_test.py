import pytest
from sympy.solvers import solve
from sympy import symbols


def func(exp):
    x = symbols('x')
    return solve(x ** exp - 1, x)


def test_one():
    assert func(2) == [-1, 1]
