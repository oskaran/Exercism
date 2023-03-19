from math import sqrt
from typing import Tuple, List, Optional


def getFactors(n: int, min_factor: int, max_factor: int) -> List[List[int]]:
    """
    For i to be a factor of n, the condition "(n // i) <= max_factor" has to be met, thus:
        (n // i) <= max_factor] --> i >= (n // max_factor)
    """
    low = n // max_factor if (n // max_factor) > min_factor else min_factor
    return [[i, n // i] for i in range(low, int(sqrt(n)) + 1) if n % i == 0]

def getPal(min_factor: int, max_factor: int, high_low: bool) -> int:
    if max_factor < min_factor:
        raise ValueError("min. is larger than max.")

    args = (max_factor ** 2, min_factor ** 2 - 1, -1) if high_low else (min_factor ** 2, max_factor ** 2 + 1)
    for n in range(*args):
        str_n = str(n)
        if str_n == str_n[::-1] and any(f[1] <= max_factor for f in getFactors(n, min_factor, max_factor)):
            return n
    return 0

def largest(min_factor: int, max_factor: int) -> Tuple[Optional[int], List[List[int]]]:
    number = getPal(min_factor, max_factor, True)

    return (number, getFactors(number, min_factor, max_factor)) if number else (None, [])

def smallest(min_factor: int, max_factor: int) -> Tuple[Optional[int], List[List[int]]]:
    number = getPal(min_factor, max_factor, False)

    return (number, getFactors(number, min_factor, max_factor)) if number else (None, [])

