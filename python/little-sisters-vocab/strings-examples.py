import string
from typing import List

def add_prefix_un(word: str) -> str:
    return 'un' + word


def make_word_groups(vwords: List[str]) -> str:
    return ' :: '.join([vwords[0]] + [vwords[0] + vwords[i] for i in range(1, len(vwords))])

def make_word_groups_1(vocab_words): #10x faster
    return (" :: " + vocab_words[0]).join(vocab_words)


def remove_suffix_ness(word: str) -> str:
    word = word.rstrip('ness')
    return word[:-1] + 'y' if word[-1] == 'i' and word[-2] in 'bcdfghjklmnpqrstvwxyz' else word


def noun_to_verb(sentence: str, index: int) -> str:
    sentence_list = sentence.split()
    return sentence_list[index].strip(string.punctuation) + 'en'
