# Bioinformatics Stronghold, Problem 8: Translating RNA to Protein
# 
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.
# 
# Sample Input:
# -------------
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# 
# Sample Output:
# --------------
# MAMAPRTEINSTRING

RNA_CODON_TABLE = {
    'UUU': 'F', 
    'UUC': 'F', 
    'UUA': 'L', 
    'UUG': 'L', 
    'UCU': 'S', 
    'UCC': 'S', 
    'UCA': 'S', 
    'UCG': 'S', 
    'UAU': 'Y', 
    'UAC': 'Y', 
    'UAA': 'Stop', 
    'UAG': 'Stop', 
    'UGU': 'C', 
    'UGC': 'C', 
    'UGA': 'Stop', 
    'UGG': 'W', 
    'CUU': 'L', 
    'CUC': 'L', 
    'CUA': 'L', 
    'CUG': 'L', 
    'CCU': 'P', 
    'CCC': 'P', 
    'CCA': 'P', 
    'CCG': 'P', 
    'CAU': 'H', 
    'CAC': 'H', 
    'CAA': 'Q', 
    'CAG': 'Q', 
    'CGU': 'R', 
    'CGC': 'R', 
    'CGA': 'R', 
    'CGG': 'R', 
    'AUU': 'I', 
    'AUC': 'I', 
    'AUA': 'I', 
    'AUG': 'M', 
    'ACU': 'T', 
    'ACC': 'T', 
    'ACA': 'T', 
    'ACG': 'T', 
    'AAU': 'N', 
    'AAC': 'N', 
    'AAA': 'K', 
    'AAG': 'K', 
    'AGU': 'S', 
    'AGC': 'S', 
    'AGA': 'R', 
    'AGG': 'R', 
    'GUU': 'V', 
    'GUC': 'V', 
    'GUA': 'V', 
    'GUG': 'V', 
    'GCU': 'A', 
    'GCC': 'A', 
    'GCA': 'A', 
    'GCG': 'A', 
    'GAU': 'D', 
    'GAC': 'D', 
    'GAA': 'E', 
    'GAG': 'E', 
    'GGU': 'G', 
    'GGC': 'G', 
    'GGA': 'G', 
    'GGG': 'G'
}

def convert_to_protein(mRNA):
    """
    Converts the strand of mRNA to a protein string made with the amino acid alphabet.

    Params:
    -------
    mRNA: (str)
        An RNA string corresponding to a strand of mRNA

    Returns:
    --------
    protein: (str)
        The protein string encoded by the mRNA strand. This is usually determined 
        by the ecoding of the codons by the amino acid alphabet.
    """
    protein = []
    for i in range(0, len(mRNA), 3):
        codon = mRNA[i:i+3]

        # Find the value of the codon within the table
        if codon in RNA_CODON_TABLE.keys() and RNA_CODON_TABLE.get(codon) != "Stop":
            protein.append(RNA_CODON_TABLE.get(codon))
        else:
            break
    
    return ''.join(protein)


if __name__ == "__main__":
    with open("datasets/rosalind_prot.txt", "r") as rna:
        sequence = rna.readline()

    # Convert rna to protein
    protein = convert_to_protein(sequence)
    print(protein)

    # Save result
    with open("output/008_rosalind_prot.txt", "w") as out:
        out.write(protein)