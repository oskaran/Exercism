
def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()
    if '?' in hey_bob and hey_bob.isupper():
         return "Calm down, I know what I'm doing!"
    elif hey_bob and hey_bob.endswith('?'):
        return 'Sure.'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    elif not hey_bob:
        return  'Fine. Be that way!'

    return 'Whatever.'
