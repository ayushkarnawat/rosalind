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

    Params:
    -------
    a:(int) 
        Length of 1st leg
        
    b: (int)
        Length of 2nd leg

    Returns:
    --------
    c: (int)
        Square of length of 3rd leg (hypotenuse)
    """
    return (a ** 2) + (b ** 2)

if __name__ == "__main__":
    with open("datasets/rosalind_ini2.txt", "r") as data:
        nums = data.readline()
        a, b = (int(x) for x in nums.split())

    # Save output
    with open("output/rosalind_ini2.txt", "w") as out:
        out.write(str(get_hypotenuse(a,b))