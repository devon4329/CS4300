import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task2 import give_int, give_float, give_string, give_bool

def test_int():
    assert give_int() == 448

def test_float():
    assert give_float() == 9.342

def test_string():
    assert give_string() == "LeBron is NOT the GOAT"

def test_bool():
    assert give_bool() is True
