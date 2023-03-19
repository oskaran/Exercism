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
    isbnStr = isbnRegex.findall(isbn)
    if not isbnStr:
        return False
    nums = [int(c) if c != 'X' else 10 for c in isbnStr[0][0].replace('-', '')]
    return sum(nums[i]*coef for i, coef in enumerate(list(range(10, 0, -1)))) % 11 == 0
