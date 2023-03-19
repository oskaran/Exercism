#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:39:11 2021

@author: oskar

vanguard478's solution
"""
codons_protein = {'Methionine': 	'AUG'	,
                  'Phenylalanine': 	['UUU', 'UUC'],
                  'Leucine': 	['UUA', 'UUG'],
                  'Serine': 	['UCU', 'UCC', 'UCA', 'UCG'],
                  'Tyrosine': 	['UAU', 'UAC']	,
                  'Cysteine': 	['UGU', 'UGC'],
                  'Tryptophan': 	'UGG',
                  'STOP': 	['UAA', 'UAG', 'UGA']
                  }

def proteins(strand):
    amino_acid = []
    chunks = [strand[i:i+3] for i in range(0, len(strand), 3)]
    for codon in chunks:
        proteins = next(
            key for key, values in codons_protein.items() if codon in values)

        if proteins == 'STOP':
            break
        else:
            amino_acid.append(proteins)
    return amino_acid