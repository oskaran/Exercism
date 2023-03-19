import math

def score(x: int, y: int) -> int:
    h = math.sqrt((x ** 2) + (y ** 2))
    scores = {h > 10: 0,
              5 < h <= 10: 1,
              1 < h <= 5: 5,
              h <= 1: 10}
    return scores[True]
