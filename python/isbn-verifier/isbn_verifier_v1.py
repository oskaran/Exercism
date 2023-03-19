"""
(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0

3-598-21508-8
3-598-21507-X
3598215088
"""
import re

def is_valid(isbn: str) -> bool:
    isbnRegex = re.compile(r'''(
            ^( [0-9]{1} )      # 1st number
            ( - )?          # separator
            ( [0-9]{3} )   # group three characters
            ( - )?          # separator
            ( [0-9]{5} )   # group five characters
            ( - )?          # separator
            ( [0-9X]{1} )$      # last character
            )''', re.VERBOSE)

    #isbnStr = isbnRegex.search(isbn)
    isbnStr = isbnRegex.findall(isbn)
    #if isbnStr == None:
    if not isbnStr:
        return False
    else:
        #isbnStr = isbnRegex.search(isbn).group()
        nums = [int(c) if c != 'X' else 10 for c in [d for d in isbnStr[0][0] if d != '-']]
        return sum(nums[i]*coef for i, coef in enumerate(list(range(10, 0, -1)))) % 11 == 0

