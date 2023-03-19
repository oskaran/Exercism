
def is_armstrong_number(number):
    digits = [int(c) for c in str(number)]
    return sum(d**len(digits) for d in digits) == number

