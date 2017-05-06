# Python Village, Problem 3: Strings and Lists
# 
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# 
# Return: The slice of this string from indices a through b and c through d (with 
#   space in between), inclusively. In other words, we should include elements 
#   s[a:b] and s[c:d] in our slice.
# 
# Sample Input: HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
#               22 27 97 102
# Sample Output: Humpty Dumpty 

def slice_string(s, a, b, c, d):
    """
    Slices the given string into two words with the first word having indices of a:b 
    and the second word having indicies of c:d.

    Params:
    -------
    s: (str)
        Arbitrary string with size of atmost 200 characters

    a: (int)
        Index where to start cutting first char of first word

    b: (int)
        Index where to stop cutting last char of first word

    c: (int)
        Index where to start cutting first char of second word

    d: (int)
        Index where to stop cutting last char of second word

    Returns:
    --------
    str:
        String representation of the two words cut from the inputted string
    
    """
    return s[a:b+1] + " " + s[c:d+1]

if __name__ == "__main__":
    # Parse indicies and spilt words
    with open("dataset/rosalind_ini3.txt", "r") as chars:
        string = chars.readline()
        nums = chars.readline()
        a, b, c, d = (int(x) for x in nums.split())

    # Find words
    print(slice_string(string, a, b, c, d))