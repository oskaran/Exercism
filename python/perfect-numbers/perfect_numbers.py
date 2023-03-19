
def classify(number):

    if number <= 0:
        raise ValueError("Number has to be greater than 0")

    aliquot = sum(i for i in range(1, number // 2 + 1) if number % i == 0)
    if aliquot == number:
        return 'perfect'
    elif aliquot > number:
        return 'abundant'
    else:
        return 'deficient'