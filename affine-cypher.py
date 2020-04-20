"""
Affine Encryption - Linear Cypher
(General Formula) --> y = ax + b
"""
import string

def affine_enc(a, b, word):
    word = str(word).strip()
    word = word.lower()
    alphabet = list(string.ascii_lowercase)
    cypher = []
    for letter in word:
        pos = alphabet.index(letter) + 1
        new = ((a * pos) + b) % len(alphabet)
        cypher.append(alphabet[new - 1])
    cypher = ' '.join(cypher)
    return cypher