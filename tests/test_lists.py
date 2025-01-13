from src.lists import *


def test_find_range():
    assert find_range([1, 5, 9, 2]) == 8
    assert find_range([10, 20, 30, 40]) == 30
    assert find_range([-10, -5, 0, 5, 10]) == 20
    assert find_range([7]) == 0
    assert find_range([]) == 0

def test_even_odd_difference():
    assert even_odd_difference([1, 2, 3, 4, 5]) == -3
    assert even_odd_difference([10, 20, 30, 40]) == 100
    assert even_odd_difference([1, 3, 5, 7]) == -16
    assert even_odd_difference([2, 4, 6, 8]) == 20
    assert even_odd_difference([]) == 0

