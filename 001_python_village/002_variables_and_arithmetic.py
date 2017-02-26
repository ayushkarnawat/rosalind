# Python Village, Problem 2: Variables and Some Arithmetic
# 
# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of 
#   the right triangle whose legs have lengths a and b.
# 
# Sample Input: 3 5
# Sample Output: 34

def get_hypotenuse(a,b):
    """
    Returns the square of the hypotenuse of the triangle with legs a and b.

    params:
        a (int): length of 1st leg
        b (int): length of 2nd leg

    returns:
        c (int): square of length of 3rd leg (hypotenuse)
    """
    return (a ** 2) + (b ** 2)

if __name__ == "__main__":
    with open("dataset/rosalind_ini2.txt", "r") as nums:
        list_of_nums = nums.read()
    a = int(list_of_nums.split(' ')[0])
    b = int(list_of_nums.split(' ')[1])
    print(get_hypotenuse(a,b))