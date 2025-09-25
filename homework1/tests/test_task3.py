# Testing task3

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task3 import check_num, for_primes, the_sum

def test_check():
    assert check_num(17) == "Positive"
    assert check_num(24) == "Positive"
    assert check_num(-8234737) == "Negative"
    assert check_num(0) == "Zero"

def test_primes():
    assert for_primes(10)  == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum():
    assert the_sum(100) == 5050
