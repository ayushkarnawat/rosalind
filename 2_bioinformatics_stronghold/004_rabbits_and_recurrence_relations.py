# Bioinformatics Stronghold, Problem 4: Rabbits and Recurrence Relations
#
# Given: Positive integers n <= 40 and  k <= 5
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each 
#           generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of 
#           only 1 pair)
#
# Sample Input: 5 3
# Sample Output: 19


def fib(n, k):
    """
    Calculates the recurrence relation of fibonnaci numbers n times with each 
    step adding k more leaves to the previous tree.

    Params:
    -------
    n: (int)
        Number of times to calculate recurrence

    k: (int)
        Number of additons made at every recurrence

    Returns:
    --------
    pop: (int)
        Population (in terms of pairs of rabbits) after n months with k additions each month

    """
    pop = [0, 1, 1]
    for i in range(3, n + 1):
        new_pop = pop[i - 1] + (k * pop[i - 2])
        pop.append(new_pop)
    return pop[n]


if __name__ == "__main__":
    with open("datasets/rosalind_fib.txt", "r") as data:
        nums = data.readline()
        a, b = (int(x) for x in nums.split())

    # Calculate population after n months
    pop = fib(a, b)
    print(pop)

    # Save result
    with open("output/004_rosalind_fib.txt", "w") as out:
        out.write(str(pop))
