# Test Task 7

import pytest
import sys

sys.path.insert(0, "../src")

from task7 import calculate

def test_calc():
    input = [3, 6, 2, 5, 19, 1]
    mean, median = calculate(input)

    assert mean == 6.0
    assert median == 4.0 
