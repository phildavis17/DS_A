from math import sqrt
from typing import List

def prime_sieve(n: int) -> List[int]:
    nums = set(range(2, n + 1))
    for factor in range(2, int(sqrt(n)) + 1):
        nums -= set([factor * x for x in range(2, (n // factor) + 1)])
    return list(nums)

print(prime_sieve(11))

def is_prime(n: int) -> bool:
    possible_factors = prime_sieve(round(sqrt(n)))
    for f in possible_factors:
        if n % f == 0:
            return False
    return True

print(is_prime(10))
print(is_prime(503))
    
