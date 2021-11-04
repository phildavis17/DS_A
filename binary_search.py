import logging

from typing import Any, Iterable

logging.basicConfig(level=logging.DEBUG)

simple_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
empty_list = []
one_list = [1]
two_list = [1, 2]
three_list = [1, 2, 3]


def bin_search(l:Iterable, target: Any) -> int:
    """
    If target is found, returns index of target. If not found return -1.
    """
    low = 0
    high = len(l) - 1
    found = False
    
    while not found and high >= low:
        pivot = low + ((high - low) // 2)
        #logging.debug(f"{pivot=}")
        if l[pivot] == target:
            found = True
            break
        elif l[pivot] < target:
            low = pivot + 1
        elif l[pivot] > target:
            high = pivot - 1
    if found:
        return pivot
    else:
        return -1


if __name__ == "__main__":
    print(bin_search(three_list, 1))