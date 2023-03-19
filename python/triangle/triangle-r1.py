from typing import List, Union

def equilateral(sides: List[Union[int, float]]) -> bool:
    x, y, z = sides[0], sides[1], sides[2]
    return True if isTriangle(x, y, z) and x == y and x == z else False

def isosceles(sides: List[Union[int, float]]) -> bool:
    x, y, z = sides[0], sides[1], sides[2]
    return True if isTriangle(x, y, z) and (x == y or x == z or y == z) else False

def scalene(sides: List[Union[int, float]]) -> bool:
    x, y, z = sides[0], sides[1], sides[2]
    return True if isTriangle(x, y, z) and x != y and x != z and y != z else False

def isTriangle(x: Union[int, float], y: Union[int, float], z: Union[int, float]) -> bool:
    # z ≤ x + y: the sum of the lengths of any two sides must be greater than or equal
    # to the length of the third side.
    if all([x, y, z]) and (x + y) >= z and (x + z) >= y and (y + z) >= x:
        return True
    else:
        return False

