from typing import List, Union

def equilateral(sides: List[Union[int, float]]) -> bool:
    return True if isTriangle(sides) and len(set(sides)) == 1 else False

def isosceles(sides: List[Union[int, float]]) -> bool:
    return True if isTriangle(sides) and len(set(sides)) < 3 else False

def scalene(sides: List[Union[int, float]]) -> bool:
    return True if isTriangle(sides) and len(set(sides)) == 3 else False

def isTriangle(sides: List[Union[int, float]]) -> bool:
    # z ≤ x + y: the sum of the lengths of any two sides must be greater than or equal
    # to the length of the third side.
    x ,y, z = sorted(sides)
    return True if all(sides) and (x + y) >= z else False

