from typing import List

def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    def freqDict(wrd):
        fdict = {}
        for c in wrd.lower():
            fdict[c] = fdict.get(c,0) + 1
        return fdict

    word_dict = freqDict(word)
    candidates_uniq = [c for c in candidates if word.lower() != c.lower()]
    ldic_words = [freqDict(s) for s in candidates_uniq]
    return [candidates_uniq[i] for i, d in enumerate(ldic_words) if word_dict == d]

# feeshoo
def find_anagrams1(word, candidates):
    return [candidate for candidate in candidates if sorted(word.lower()) == sorted(candidate.lower()) and word.lower() != candidate.lower()]

# Agathasta
def find_anagrams2(word: str, candidates: List[str]) -> List[str]:

    return [cand for cand in candidates
            if cand.lower() != word.lower()
            and sorted(cand.lower()) == sorted(word.lower())]

def find_anagrams3(word, candidates):
    word = word.lower()
    return [c for c in candidates if sorted(word) == sorted(c.lower()) and word != c.lower()]