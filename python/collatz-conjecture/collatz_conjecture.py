def steps(number):
    if number <= 0:
        raise ValueError("Not a positive integer")
    count = 0
    while number > 1:
        number = number // 2 if number % 2 == 0 else 3 * number + 1
        count += 1

    return count