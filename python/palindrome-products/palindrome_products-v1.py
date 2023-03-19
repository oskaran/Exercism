"""
Detect palindrome products in a given range.
A palindromic number is a number that remains the same when its digits are reversed.
For example, 121 is a palindromic number but 112 is not.
    Given a range of numbers, find the largest and smallest palindromes which are products
of numbers within that range.
Your solution should return the largest and smallest palindromes, along with the factors
of each within the range. If the largest or smallest palindrome has more than one pair of
factors within the range, then return all the pairs.

"""
import math
from typing import Tuple, List

def isPal(s: str) -> bool:
    return True if len(s) <= 1 else s[0] == s[-1] and isPal(s[1:-1])

# def products(min_factor: int, max_factor: int) -> Set[int]:
#     return {a * b for a, b in [(i, j) for i in range(min_factor, (max_factor + 1))
#                              for j in range(min_factor, (max_factor + 1))]}

def largest(min_factor: int, max_factor: int) -> Tuple[int, List[List[int]]]:
    # p = {a * b for a, b in [(i, j) for i in range(min_factor, (max_factor + 1))
    #                          for j in range(min_factor, (max_factor + 1))]}
    # number = max([i for i in p if isPal(str(i))])
    if max_factor - min_factor < 0:
        raise ValueError("min is more than max")
    # number = 0
    # for i in range(max_factor, (min_factor - 1), -1):
    #     for j in range(max_factor, (min_factor - 1), -1):
    #         if isPal(str(i * j)):
    #             number = i * j
    #             break
    #     if number:
    #         break
    #     else:
    #         continue
    number = max(i * j for i in range(max_factor, (min_factor - 1), -1)
                 for j in range(max_factor, (min_factor - 1), -1) if isPal(str(i * j)))
    #factors = [[i, number // i] for i in range(1, int(math.sqrt(number)) + 1) if number % i == 0]
    factors = [[i, number // i] for i in range(int(math.sqrt(number)), 0, -1) if number % i == 0
               and i <= max_factor and (number // i) <= max_factor]
    return (number, factors) if number else (None, factors)

def smallest(min_factor: int, max_factor: int) -> Tuple[int, List[List[int]]]:
    # p = {a * b for a, b in [(i, j) for i in range(min_factor, (max_factor + 1))
    #                          for j in range(min_factor, (max_factor + 1))]}
    # number = min([i for i in p if isPal(str(i))])
    if max_factor - min_factor < 0:
        raise ValueError("min is more than max")
    # number = 0
    # for i in range(min_factor, (max_factor + 1)):
    #     for j in range(min_factor, (max_factor + 1)):
    #         if isPal(str(i * j)):
    #             number = i * j
    #             break
    #     if number:
    #         break
    #     else:
    #         continue
    number = min(i * j for i in range(min_factor, (max_factor + 1))
                 for j in range(min_factor, (max_factor + 1)) if isPal(str(i * j)))
    #factors = [[i, number // i] for i in range(1, int(math.sqrt(number)) + 1) if number % i == 0]
    factors = [[i, number // i] for i in range(int(math.sqrt(number)), 0, -1) if number % i == 0
               and i >= min_factor and (number // i) >= min_factor]
    return (number, factors) if number else (None, factors)


#list({a * b for a, b in [(i, j) for i in range(1, 10) for j in range(1, 10)]})

"""
1..trunc(:math.sqrt(number))
      |> Enum.filter(&(rem(number, &1) == 0))
      |> Enum.flat_map(&([&1, div(number, &1)]))

fn x -> [x, div(number, x)]

Enum.join(Enum.map(String.split("hello, world!", " "), &String.capitalize/1), " ")

or having many intermediate "throw-away variables"

string = "hello, world!"
words = String.split(string, " ")
capitalized_words = Enum.map(words, &String.capitalize/1)
Enum.join(capitalized_words, " ")

you can use the pipe operator to write

"hello, world!"
|> String.split(" ")
|> Enum.map(&String.capitalize/1)
|> Enum.join

Enum.join(Enum.map(String.split("hello, world!", " "), &String.capitalize/1), " ")

factors = []
for(x = 1; x <= sqrt(n); x++){
    if(n % x == 0){
        factors.add(x)
        factors.add(n / x)
    }
}

"""