
def convert(number):
    out = ''
    if number % 3 == 0: out += 'Pling'
    if number % 5 == 0: out += 'Plang'
    if number % 7 == 0: out += 'Plong'
    if not out:         out = str(number)
    return out



