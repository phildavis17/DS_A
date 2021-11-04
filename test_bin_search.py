import pytest

from binary_search import bin_search

basic_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
empty_list = []
one_list = [1]
two_list = [0, 1]
three_list = [1, 2, 3]


def test_basic_bin_search():
    assert bin_search(basic_list, 4) == 4


def test_bin_search_not_found():
    assert bin_search(basic_list, 20) == -1


def test_boundary_search():
    assert bin_search(basic_list, 0) == 0
    assert bin_search(basic_list, 9) == 9

def test_one_item():
    assert bin_search(one_list, 1) == 0
    assert bin_search(one_list, 2) == -1

def test_two_items():
    assert bin_search(two_list, 0) == 0
    assert bin_search(two_list, 1) == 1
    assert bin_search(two_list, 2) == -1
    assert bin_search(two_list, -1) == -1

def test_three_item():
    assert bin_search(three_list, 0) == -1
    assert bin_search(three_list, 1) == 0
    assert bin_search(three_list, 2) == 1
    assert bin_search(three_list, 3) == 2
    assert bin_search(three_list, 4) == -1

def test_empty_list():
    assert bin_search(empty_list, 0) == -1