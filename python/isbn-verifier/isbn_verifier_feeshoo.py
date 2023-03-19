import re

def is_valid(isbn:str) -> bool:
    isbn_str = isbn.replace("-","")
    if not re.match(r"\d{9}[\dX]{1}", isbn_str) or len(isbn_str) != 10:
        return False
    isbn_nums = [10 if num == "X" else int(num) for num in isbn_str]
    return sum(map(lambda x,y: x*y, isbn_nums, range(10, 0, -1))) % 11 == 0