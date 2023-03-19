def is_isogram(string: str) -> bool:
    string = string.lower().replace('-', '').replace(' ', '')

    return len(string) == len(set(string))
