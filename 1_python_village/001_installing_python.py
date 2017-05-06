# Python Village, Problem 1: Installing Python
# 
# After downloading and installing Python, type import this into the Python 
#   command line and see what happens. Then, click the "Download dataset" 
#   button below and copy the Zen of Python into the space provided.

import sys

if __name__ == "__main__":
    with open("output/rosalind_ini1.txt", "w") as out:
        sys.stdout = out
        import this