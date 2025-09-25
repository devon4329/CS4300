import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task4 import calculate_discount

def test_ints():
    assert calculate_discount(100, 10) == 90.00
    assert calculate_discount(100, 50) == 50.00

def test_floats():
    assert calculate_discount(99.99, 10.5) == 89.49
    assert calculate_discount(150.75, 25.0) == 113.06

def test_mix():
    assert calculate_discount(100, 12.5) == 87.5
    assert calculate_discount(250.50, 50) == 125.25


