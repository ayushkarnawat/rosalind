# Bioinformatics Stronghold, Problem 2: Transcribing DNA into RNA
# 
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is 
# 	formed by replacing all occurrences of 'T' in t with 'U' in u. 
# 
# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t
# 
# Sample Input: GATGGAACTTGACTACGTAAATT
# Sample Output: GAUGGAACUUGACUACGUAAAUU

from enum import Enum

class DNA(Enum):
	"""Represents the various nucleotides that can be within a given DNA string."""
	A = "A"
	C = "C"
	G = "G"
	T = "T"

class RNA(Enum):
	"""Represents the various nucleotides that can be within a given RNA string."""
	A = "A"
	C = "C"
	G = "G"
	U = "U"

def convert_dna_to_rna(dna):
	"""
	Transcribes the given DNA sequence into RNA.
	
	params:
		dna (str): A collection of nucleotides (A,C,G,T)
			i.e. "GATGGAACTTGACTACGTAAATT"

	returns:
		rna (str): A collection of nucleotides (A,C,G,U)
			i.e. "GAUGGAACUUGACUACGUAAAUU"
	"""
	rna = []
	for nucleotide in dna:
		if (nucleotide == DNA.A.value):
			rna.append(RNA.A.value)
		elif (nucleotide == DNA.C.value):
			rna.append(RNA.C.value)
		elif (nucleotide == DNA.G.value):
			rna.append(RNA.G.value)
		else:
			rna.append(RNA.U.value)
	return ''.join(rna) # combines the list of nucleotides in rna into a string

if __name__ == "__main__":
	with open("dataset/002_rosalind_rna.txt", "r") as dna:
		sequence = dna.read()
	print(convert_dna_to_rna(sequence))
