"""
Problem: You are given an integer N, . Your task is to print an alphabet rangoli of size N 

Platform : HackerRank

Difficulty: Mid

"""


import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3

    lines = []

    for i in range(size):
        # Create the descending and ascending parts
        part = alphabet[i:size]
        pattern = "-".join(part[::-1] + part[1:])

        # Center the pattern using hyphens
        lines.append(pattern.center(width, "-"))

    # Print the upper half and lower half
    print("\n".join(lines[::-1] + lines[1:]))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)