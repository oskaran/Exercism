import random

def private_key(p: int) -> int:
    return random.randint(2, p - 1) 


def public_key(p: int, g: int, private: int) -> int:
    return pow(g, private, p)


def secret(p: int, public: int, private: int) -> int:
    return pow(public, private, p)
