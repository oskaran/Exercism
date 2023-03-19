dna_2_rna: dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand: str) -> str:
    return ''.join([dna_2_rna[n] for n in dna_strand])
