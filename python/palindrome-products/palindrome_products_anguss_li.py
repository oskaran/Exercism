#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 20:04:51 2021

@author: oskar
anguss-li's solution
"""
from typing import List, Tuple


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


def largest(min_factor: int, max_factor: int) -> Tuple[int, List[List[int]]]:
    '''
    Return the largest palindromic number in the range between min_factor and
    max_factor (both inclusive) as well as said number's factors
    '''
    palindrome = get_palindrome(min_factor, max_factor, reverse=True)
    return palindrome, get_factors(palindrome, min_factor, max_factor)


def smallest(min_factor: int, max_factor: int) -> Tuple[int, List[List[int]]]:
    '''
    Return the smallest palindromic number in the range between min_factor and
    max_factor (both inclusive) as well as said number's factors
    '''
    palindrome = get_palindrome(min_factor, max_factor)
    return palindrome, get_factors(palindrome, min_factor, max_factor)