# Rosalind, Problem 3: Complementing a Strand of DNA
# 
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols 
#   of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# 
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
# 
# Sample Input: AAAACCCGGT
# Sample Output: ACCGGGTTTT

from enum import Enum

class DNA(Enum):
	"""Represents the various nucleotides that can be within a given DNA string."""
	A = "A"
	C = "C"
	G = "G"
	T = "T"

def reverse(dna):
	"""
	Reverses the given string.
	
	params:
		dna (str): A string of nucleotides constructed from the alphabet {A,C,G,T}
			i.e. "AAAACCCGGT"
	
	returns:
		reversed_dna (str): The reversed form of the DNA string
			i.e. "TGGCCCAAAA"
	"""
	return dna[::-1]

def reverse_complement(dna):
	"""
	Finds the complement of the given DNA strand. 

	params:
		dna (str): A string of nucleotides constructed from the alphabet {A,C,G,T}
			i.e. "AAAACCCGGT"

	returns:
		complement (str): The complement form of the DNA string
			i.e. "ACCGGGTTTT"
	"""
	complement = []
	for nucleotide in reverse(dna):
		if (nucleotide == DNA.A.value):
			complement.append(DNA.T.value)
		elif (nucleotide == DNA.C.value):
			complement.append(DNA.G.value)
		elif (nucleotide == DNA.G.value):
			complement.append(DNA.C.value)
		elif (nucleotide == DNA.T.value):
			complement.append(DNA.A.value)
	return ''.join(complement) # combines the reversed list of nucleotides into a string

if __name__ == "__main__":
	with open("dataset/003_rosalind_revc.txt", "r") as dna:
		sequence = dna.read()
	print(reverse_complement(sequence))
