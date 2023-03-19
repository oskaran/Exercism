# https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# x or y : "if x is false, then y, else x"
# This is a short-circuit operator, so it only evaluates the second argument if the first one is false.
def convert(number):
    out = ''
    if number % 3 == 0:
        out += 'Pling'
    if number % 5 == 0:
        out += 'Plang'
    if number % 7 == 0:
        out += 'Plong'
    # x or y : if x is false, then y, else x
    return out or str(number)
    # if not out:
    #     out = str(number)
    # return out