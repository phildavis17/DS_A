import logging

from typing import Any, Sized

logging.basicConfig(level=logging.DEBUG)

simple_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
empty_list = []
one_list = [1]
two_list = [1, 2]
three_list = [1, 2, 3]


def bin_search(l:Sized, target: Any) -> int:
    """
    If target is found, returns index of target. If not found return -1.
    """
    low = 0
    high = len(l)
    found = False
    
    while not found and high > low:
        pivot = (low + high) // 2
        if l[pivot] == target:
            found = True
            break
        elif l[pivot] < target:
            low = pivot + 1
        else:
            high = pivot
    if found:
        return pivot
    else:
        return -1


def bin_search_basic(l: Sized, target: Any) -> int:
    """

    """
    low = 0
    high = len(l)

    while low < high:
        mid = (high + low) // 2
        hot = l[mid]
        if  hot == target:
            return mid
        elif hot < target:
            low = mid + 1
        else:
            high = mid
        


if __name__ == "__main__":
    print(bin_search(three_list, 1))