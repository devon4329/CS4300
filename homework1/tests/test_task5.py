# Test Lists and Dictionaries

# test_task5.py
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task5 import fav_books, first_three, student_db, get_name


def test_books():
    # Ensure each book is a dictionary with 'title' and 'author'
    for key in fav_books:
        if key in range (len(fav_books)):
            assert "title" in book
            assert "author" in book


def test_first_books():
    first_books = first_three()
    assert len(first_books) == 3
  
    assert first_books == fav_books[:3]


def test_student_db():
   
    for id, name in student_db.items():
        assert isinstance(id, int)
        assert isinstance(name, str)


def test_get_name():
    assert get_name(102) == "Jane Doe"
    assert get_name(104) == "Leroy Jenkins"
    assert get_name(107) is None
