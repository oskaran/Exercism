
def transform(legacy_data: dict) -> dict:
    return {letter.lower():score for score, letters in legacy_data.items() \
            for letter in letters}
