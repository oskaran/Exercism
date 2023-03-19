
def proteins(strand):
    codons = {"AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "stop",
    "UAG": "stop",
    "UGA": "stop"}

    prot = []
    for i in range(0, len(strand), 3):
        c = strand[i:i+3]
        if c in codons.keys() and codons[c] != 'stop':
            prot.append(codons[c])
        else:
            break
    return prot


