import re

def is_valid(isbn: str) -> bool:
    # Remove dashes and convert to list
    list_isbn = re.findall(r'\w', isbn)

    # False if list length is not 10 OR string[0:9] contains letters OR string[last] is not digit or X
    if len(list_isbn) != 10 or re.search(r'[^-\d]', isbn[:-1]) or re.match(r'[^X\d]', isbn[-1]):
        return False

    list_isbn[-1] = '10' if list_isbn[-1] == 'X' else list_isbn[-1]

    return sum(int(n) * i for i, n in enumerate(list_isbn[::-1], start=1)) % 11 == 0