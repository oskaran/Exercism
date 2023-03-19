
from typing import List

def value(colors: List[str]) -> int:
    res_colors = ['black','brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet','grey', 'white'] 

    return (10 * res_colors.index(colors[0]) + res_colors.index(colors[1]))
