
import math
from typing import Tuple, List, Optional, Iterator

def isPal(s: str) -> bool:
    return True if len(s) <= 1 else s[0] == s[-1] and isPal(s[1:-1])

def numbers(min_factor: int, max_factor: int) -> Iterator[int]:
    if max_factor - min_factor < 0:
        raise ValueError("min is more than max")

    return (i * j for i in range(min_factor, (max_factor + 1))
                 for j in range(min_factor, (max_factor + 1)) if isPal(str(i * j)))

def largest(min_factor: int, max_factor: int) -> Tuple[Optional[int], List[List[int]]]:
    number = max(numbers(min_factor, max_factor), default=0)
    factors = [[i, number // i] for i in range(int(math.sqrt(number)), 0, -1) if number % i == 0
                and i <= max_factor and (number // i) <= max_factor]

    return (number, factors) if number else (None, factors)

def smallest(min_factor: int, max_factor: int) -> Tuple[Optional[int], List[List[int]]]:
    number = min(numbers(min_factor, max_factor), default=0)
    factors = [[i, number // i] for i in range(int(math.sqrt(number)), 0, -1) if number % i == 0
                and i >= min_factor and (number // i) >= min_factor]

    return (number, factors) if number else (None, factors)


