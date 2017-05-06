# Python Village, Problem 4: Conditionals and Loops
# 
# Given: Two positive integers a and b (a < b< 10000)
# Return: The sum of all odd integers from a through b, inclusively.
# 
# Sample Input: 100 200
# Sample Output: 7500

def sum_odd_numbers(a,b):
    """
    Sum of all the odd numbers between two numbers a through b, inclusive.

    Params:
    -------
    a: (int)
        Number to start counting from

    b: (int)
        Number to end counting at

    Returns:
    --------
    sum: (int)
        Sum of all odd inetegers from a to b
    
    """
    sum_nums = 0
    for num in range(a,b+1):
        if (num % 2 == 1):
            sum_nums += num
    return sum_nums

if __name__ == "__main__":
    with open("dataset/rosalind_ini4.txt", "r") as data:
        nums = data.readline()
        a, b = (int(x) for x in nums.split())

    print(sum_odd_numbers(a, b))