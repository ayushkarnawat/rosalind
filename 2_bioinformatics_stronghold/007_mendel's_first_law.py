import math


def perm(n, k, replacement=True):
    """
    The number of ways to choose a subset of k elements, taking into account order, 
    from a set of n elements.

    Params:
    -------
    n: (int)
        Number of elements to choose from

    k: (int)
        Number of elements to actually chooose

    replacement: (bool)
        Whether or not repetition/replacement is allowed (i.e. should you be able
        to chose the thing/item once again).

    Returns:
    --------
    num_orderings: (int)
        The total number of ways to choose a subset of k eements from a set of n elements 
    """
    if replacement:
        return n ** k
    return math.factorial(n) / (math.factorial(n - k))


def probability(k, m, n):
    """
    Calculate the percentage that two of the random two randomly selected mating
    organisms will produce an individual possessing a dominant allele (and thus 
    displaying the dominant phenotype). We assume that any two organism can mate.

    Params:
    -------
    k: (int)
        Number of homozygous dominant individuals 

    m: (int)
        Number of heterozygous individuals

    n: (int)
        Number of homozygous recessive individuals

    Returns:
    --------
    prob: (float)
        Probability that the individual produced will hold a dominant allele. 
    """

    # Calculate the total number of dominant alleles possible
    dominant_alleles = [
        perm(k, 2, replacement=False),          # AA, AA pairs
        k * m,                                  # AA, Aa pairs
        k * n,                                  # AA, aa pairs
        m * k,                                  # Aa, AA pairs
        perm(m, 2, replacement=False) * 0.75,   # Aa, Aa pairs
        m * n * 0.5,                            # Aa, aa pairs
        n * k,                                  # aa, AA pairs
        n * m * 0.5,                            # aa, Aa pairs
        perm(n, 2, replacement=False) * 0       # aa, aa pairs
    ]

    total_alleles = perm(k + m + n, 2, replacement=False)
    return sum(dominant_alleles) / total_alleles


if __name__ == "__main__":
    with open("datasets/rosalind_iprb.txt", "r") as data:
        nums = data.readline()
        k, m, n = (int(x) for x in nums.split())

    # Calculate probability
    prob = probability(k, m, n)
    print(prob)

    with open("output/007_rosalnd_iprb.txt", "w") as out:
        out.write(str(prob))
