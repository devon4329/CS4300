import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task6 import word_count

# Test task6 using task6_read_me
def test_word_count():
    filename = os.path.join(os.path.dirname(__file__), "../src/task6_read_me.txt")
    expected_count = 104

    assert word_count(filename) == expected_count
