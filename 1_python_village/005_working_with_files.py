# Python Village, Problem 5: Working with Files
# 
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
# 
# Sample Input: 
#   Bravely bold Sir Robin rode forth from Camelot
#   Yes, brave Sir Robin turned about
#   He was not afraid to die, O brave Sir Robin
#   And gallantly he chickened out
#   He was not at all afraid to be killed in nasty ways
#   Bravely talking to his feet
#   Brave, brave, brave, brave Sir Robin
#   He beat a very brave retreat
#   
# Sample Output: 
#   Yes, brave Sir Robin turned about
#   And gallantly he chickened out
#   Bravely talking to his feet
#   He beat a very brave retreat

def get_even_lines(lines):
    """
    Get every even line from the given lines

    Params:
    -------
    lines: (list)
        A list of strings containing words

    Returns:
    --------
    even_lines: (list)
        A list of strings containing each even line of the original input
    
    """
    return [lines[i] for i in range(1, len(lines), 2)]


if __name__ == "__main__":
    with open("datasets/rosalind_ini5.txt", "r") as input_data:
        lines = [line.strip() for line in input_data.readlines()]

    # Get all even lines
    even_lines = get_even_lines(lines)

    # Save output
    with open("output/rosalind_ini5.txt", "w") as out:
        for line in even_lines:
            out.write(line + '\n')