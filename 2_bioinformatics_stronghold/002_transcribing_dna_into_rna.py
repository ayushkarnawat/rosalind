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


def convert_dna_to_rna(dna):
    """
    Transcribes the given DNA sequence into RNA.

    Params:
    -------
    dna: (str)
        A collection of various nucleotides (A,C,G,T)

    Returns:
    --------
    rna: (str)
        A collection of nucleotides (A,C,G,U)
    """
    # Replace all occurences of T with U
    return dna.replace("T", "U")


if __name__ == "__main__":
    with open("datasets/rosalind_rna.txt", "r") as dna:
        sequence = dna.read()

    # Convert sequence
    rna = convert_dna_to_rna(sequence)

    # Save output
    with open("output/002_rosalind_rna.txt", "w") as out:
        out.write(convert_dna_to_rna(sequence))