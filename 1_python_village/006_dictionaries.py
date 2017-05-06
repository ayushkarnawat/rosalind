# Python Village, Problem 6: Dictionaries
#
# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces.
#           Words are case-sensitive, and the lines in the output can be in any order.
#
# Sample Input:
#   We tried list and we tried dicts also we tried Zen
#
# Sample Output:
#   and 1
#   We 1
#   tried 3
#   dicts 1
#   list 1
#   we 2
#   also 1
#   Zen 1


def construct_dict(words):
    """
    Constructs a dictonary of words with key being the word itself and the 
    value being the number of occurences of that word in the sentence. 

    Params:
    -------
    words: (list)
        List of words of type str

    Returns:
    --------
    word_dict: (dict)
        A dictionary of words with key being the word itself and value determining 
        the number of times that word appeared in the sentence. Note: the words 
        are care sensitive so `Hi` will be counted differently from `hi`
    """
    word_dict = {}
    for word in words:
        # if not in dictonary already add it
        if word not in word_dict:
            word_dict[word] = 1
        # add 1 for every word that is the same
        else:
            word_dict[word] = word_dict[word] + 1
    return word_dict


if __name__ == "__main__":
    with open("datasets/rosalind_ini6.txt", "r") as data:
        words = data.readline().split(' ')

    # Construct a dictionary of words
    dict_of_words = construct_dict(words)

    # Save output
    with open("output/rosalind_ini6.txt", "w") as out:
        for key, value in dict_of_words.items():
            out.write(str(key) + " " + str(value) + '\n')
