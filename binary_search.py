from typing import Any, Iterable


simple_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
empty_list = []
one_list = [1]
two_list = [1, 2]
three_list = [1, 2, 3]


def bin_search(l:Iterable, target: Any) -> int:
    low = 0
    high = len(l) - 1
    pivot = low + ((high - low) // 2)
    found = False
    
    while high > low:
        if l[pivot] == target:
            break
        elif pivot < target:
            low = pivot + 1
        elif pivot > target:
            high = pivot - 1
        pivot = low + ((high - low) // 2)
    return pivot
            
print(bin_search(simple_list, 0))
print(bin_search(simple_list, 9))