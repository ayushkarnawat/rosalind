# Bioinformatics Stronghold, Problem 5: Computing GC Content
# 
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# 
# Return: The ID of the string having the highest GC-content, followed by the 
#   GC-content of that string. Rosalind allows for a default error of 0.001 in
#   all decimal answers unless otherwise stated; please see the note on absolute 
#   error below.
# 
# Sample Input:
# ------------- 
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT
# 
# Sample Output:
# --------------
# Rosalind_0808
# 60.919540

from enum import Enum
from collections import defaultdict


class DNA(Enum):
    """Represents the various nucleotides that can be within a given DNA string."""
    A = "A"
    C = "C"
    G = "G"
    T = "T"


def count_nucleotides(dna):
    """
    Counts the total number of each type of nucleotide in the given DNA string.

    Params:
    -------
    dna: (str)
        A collection of various nucleotides

    Returns:
    --------
    dna_counts: (list)
        Represents the number of each type of nucleotide in the order (A,C,T,G)
    """
    return dna.count(DNA.A.value), dna.count(DNA.C.value), dna.count(DNA.G.value), dna.count(DNA.T.value)


def gc_content(dna):
    """
    Compute the density of G's and C's in the DNA string. Usually the density 
    is represented between 0 and 1, however we want to represent this as a 
    percentage (between 0-100). 

    Params:
    -------
    dna: (str)
        A collection of various nucleotides

    Returns:
    --------
    percentage: (float)
        The percentage of G's and C's in the DNA string
    """

    # Calculate the number of each type of dna nucleotides in the dna
    num_a, num_c, num_g, num_t = count_nucleotides(dna)

    num_gc = num_c + num_g
    num_nucleotides = len(dna)

    return (num_gc / num_nucleotides) * 100


def read_fasta(filepath):
    """
    Read a FASTA-based text file and parse its inputs.abs

    Params:
    -------
    filepath: (str)
        A relative or absolute path to the file that needs to be read

    Returns:
    --------
    records: (dict)
        Returns a dictionary of (key, value) pairs with the key being the FASTA 
        name with the DNA string associated with each of the keys
    """
    with open(filepath, "r") as data:
        records = defaultdict()
        record_id = None

        # Read each individual line
        for line in [l.strip() for l in data.readlines()]:

            # Check for fasta formatted name and add that as a list
            if line.startswith('>'):
                record_id = line[1:]
            else:
                # Append the genomic sequence associated with that name
                records.setdefault(record_id, []).append(line)

        # Combine the list together into a string
        for key, value in records.items():
            records[key] = ''.join(value)

    return records


if __name__ == "__main__":
    records = read_fasta('datasets/rosalind_gc.txt')

    # Calculate gc content for each key in dictionary
    for key, value in records.items():
        records[key] = gc_content(value)

    # Find max (key, value) pair in dictionary
    max_key = max(records, key=records.get)
    max_value = max(records.values())

    # Save result
    with open("output/005_rosalind_gc.txt", "w") as out:
        out.write(str(max_key) + '\n')
        out.write(str(max_value))
    