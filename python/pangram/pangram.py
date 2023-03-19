def is_pangram(sentence):
    alpha = {c for c in 'abcdefghijklmnopqrstuvwxyz'}
    sent_set = {c for c in sentence.lower() if c in alpha}

    return sent_set == alpha

