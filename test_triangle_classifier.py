import pytest
from triangle_classifier import classify_triangle

def test_equilateral_triangle():
    result = classify_triangle(2, 2, 2)
    assert result == "Equilateral triangle"

def test_isosceles_triangle():
    result = classify_triangle(5, 5, 3)
    assert result == "Isosceles triangle"

def test_scalene_triangle():
    result = classify_triangle(3, 4, 5)
    assert result == "Scalene right triangle"

def test_right_triangle():
    result = classify_triangle(6, 8, 10)
    assert result == "Right triangle"

def test_invalid_triangle_negative_sides():
    result = classify_triangle(-1, 2, 3)
    assert result == "Invalid triangle (side lengths must be positive)"

def test_invalid_triangle_not_forming_triangle():
    result = classify_triangle(1, 2, 5)
    assert result == "Invalid triangle (the sum of any two sides must be greater than the third side)"

def test_edge_case_very_small_values():
    result = classify_triangle(0.00001, 0.00002, 0.00003)
    assert result == "Scalene triangle"

def test_edge_case_nearly_right_triangle():
    result = classify_triangle(3, 4, 5.0000001)
    assert result == "Scalene triangle"  # Very close to right, but not exactly