
from math import sqrt
from typing import Tuple, List, Optional, Iterator

def isPal(s: str) -> bool:
    return True if len(s) <= 1 else s[0] == s[-1] and isPal(s[1:-1])

def numbers(min_factor: int, max_factor: int) -> Iterator[int]:
    if max_factor - min_factor < 0:
        raise ValueError("min is more than max")

    return (i * j for i in range(min_factor, (max_factor + 1))
                  for j in range(min_factor, (max_factor + 1)) if isPal(str(i * j)))

# Guest function
def get_factors(n: int, min_factor: int, max_factor: int) -> List[List[int]]:
    '''
    Return all factors of n within the range between min_factor and max_factor
    '''
    if n == None:
        return []

    # For a integer i in range(min_factor, max_factor) to be a valid factor of
    # n, n//i <= max_factor must be True. This evaluates to i >= n//max_factor.
    min_i = n // max_factor
    lower = min_factor if min_factor > min_i else min_i

    square_root = int(n ** 0.5)
    upper = (max_factor if max_factor < square_root else square_root) + 1

    return [[i, n // i] for i in range(lower, upper) if n % i == 0]

"""
Here, you were looking for the factors from 0 to sqrt(n), bad idea
"""
def getFactors(n: int, min_factor: int, max_factor: int) -> List[List[int]]:
    """
    For i to be a factor of n, the condition "(n // i) <= max_factor" has to be met, thus:
        (n // i) <= max_factor] --> i >= (n // max_factor)
    """
    low = n // max_factor if (n // max_factor) > min_factor else min_factor
    return [[i, n // i] for i in range(low, int(sqrt(n)) + 1) if n % i == 0]

"""
def getFactors(n: int, min_factor: int, max_factor: int) -> List[List[int]]:
    #(number // i) <= max_factor] -> i >= (number // max_factor)
    #low = min_factor if min_factor > (n // max_factor) else n // max_factor
    #low = n // max_factor
    #return [[i, n // i] for i in range(int(sqrt(n)), low - 1, -1) if n % i == 0]
    return [[i, n // i] for i in range(n // max_factor, int(sqrt(n)) + 1) if n % i == 0]
"""

# Guest function
def get_palindrome(lower: int, upper: int, reverse: bool = False) -> int:
    '''
    Return the first palindromic number in the range which has factors that are
    also all within range; if reverse = True, return the last palindrome
    '''
    if lower > upper:
        raise ValueError("Minimum larger than maximum")
    args = (upper ** 2, lower**2 - 1, -1) if reverse else (lower ** 2, upper**2 + 1)
    for x in range(*args):
        x_str = str(x)
        if x_str == x_str[::-1] and any(upper >= f[1] for f in get_factors(x, lower, upper)):
            return x
    return None

def getPal(min_factor: int, max_factor: int, high_low: bool) -> int:
    if max_factor < min_factor:
        raise ValueError("min. is larger than max.")

    args = (max_factor ** 2, min_factor ** 2 - 1, -1) if high_low else (min_factor ** 2, max_factor ** 2 + 1)
    for n in range(*args):
        str_n = str(n)
        if str_n == str_n[::-1] and any(f[1] <= max_factor for f in getFactors(n, min_factor, max_factor)):
            return n
    return 0

# This is actually a 5ms faster than the version that checked the second member of the list
def getPal_a1(min_factor: int, max_factor: int, high_low: bool) -> int:
    if max_factor < min_factor:
        raise ValueError("min. is larger than max.")

    args = (max_factor ** 2, min_factor ** 2 - 1, -1) if high_low else (min_factor ** 2, max_factor ** 2 + 1)
    for n in range(*args):
        str_n = str(n)
        if str_n == str_n[::-1] and any(getFactors(n, min_factor, max_factor)):
            return n
    return 0

def largest(min_factor: int, max_factor: int) -> Tuple[Optional[int], List[List[int]]]:
    number = getPal(min_factor, max_factor, True)

    return (number, getFactors(number, min_factor, max_factor)) if number else (None, [])

def smallest(min_factor: int, max_factor: int) -> Tuple[Optional[int], List[List[int]]]:
    number = getPal(min_factor, max_factor, False)

    return (number, getFactors(number, min_factor, max_factor)) if number else (None, [])

def largest_guest(min_factor: int, max_factor: int) -> Tuple[int, List[List[int]]]:
    '''
    Return the largest palindromic number in the range between min_factor and
    max_factor (both inclusive) as well as said number's factors
    '''
    palindrome = get_palindrome(min_factor, max_factor, reverse=True)
    return palindrome, get_factors(palindrome, min_factor, max_factor)

def smallest_guest(min_factor: int, max_factor: int) -> Tuple[int, List[List[int]]]:
    '''
    Return the smallest palindromic number in the range between min_factor and
    max_factor (both inclusive) as well as said number's factors
    '''
    palindrome = get_palindrome(min_factor, max_factor)
    return palindrome, get_factors(palindrome, min_factor, max_factor)

def largest_1(min_factor: int, max_factor: int) -> Tuple[Optional[int], List[List[int]]]:
    number = max(numbers(min_factor, max_factor), default=0)
    factors = [[i, number // i] for i in range(int(sqrt(number)), 0, -1) if number % i == 0
                #and i <= max_factor and (number // i) <= max_factor]
                and (number // i) <= max_factor]
    return (number, factors) if number else (None, factors)

def smallest_1(min_factor: int, max_factor: int) -> Tuple[Optional[int], List[List[int]]]:
    number = min(numbers(min_factor, max_factor), default=0)
    factors = [[i, number // i] for i in range(int(sqrt(number)), 0, -1) if number % i == 0
                #and i >= min_factor and (number // i) >= min_factor]
                and (number // i) <= max_factor]

    return (number, factors) if number else (None, factors)

def getPal_1(min_factor: int, max_factor: int, high_low: bool) -> int:
    if min_factor > max_factor:
        raise ValueError("Minimum larger than maximum")

    args = (max_factor**2, min_factor**2 - 1, -1) if high_low else (min_factor**2, max_factor**2 + 1)
    for n in range(*args):
        factors = get_factors(n, min_factor, max_factor)
        n_str = str(n)
        #if n_str == n_str[::-1] and  any(max_factor >= f[1] for f in get_factors(n, min_factor, max_factor)):
        if n_str == n_str[::-1] and any(max_factor >= f[1] for f in factors):
                return n
    return 0

def getPal_2(min_factor: int, max_factor: int, high_low: bool) -> int:
    if min_factor > max_factor:
        raise ValueError("Minimum larger than maximum")

    args = (max_factor**2, min_factor**2 - 1, -1) if high_low else (min_factor**2, max_factor**2 + 1)
    for x in range(*args):
        x_str = str(x)
        if x_str == x_str[::-1] and any(max_factor >= f[1] for f in get_factors(x, min_factor, max_factor)):
            return x
    return 0

