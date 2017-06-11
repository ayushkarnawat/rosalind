# Bioinformatics Stronghold, Problem 6: Counting Point Mutations
#
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).
#
# Sample Input:
# -------------
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
#
# Sample Output:
# --------------
# 7


def hamming_distance(s1, s2):
    """
    Return the Hamming distance between equal-length sequences.

    Params:
    -------
    s1: (str)
        A collection characters derived from a collection of alphabet

    s2: (str)
        Another collection of characters derived from a collection of alphabet. 
        Usually, it is the same length as the first argument

    Returns:
    --------
    distance: (int)
        The number of changes needed to be made in order for both strings to 
        be the same
    """
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))


if __name__ == "__main__":
    with open("datasets/rosalind_hamm.txt", "r") as data:
        sequences = [line.strip() for line in data.readlines()]
    
    # Compute number of edits needed to be made for one string to be the same as the second
    edit_distance = hamming_distance(sequences[0], sequences[1])

    # Save result
    with open("output/006_rosalind_hamm.txt", "w") as out:
        out.write(str(edit_distance))