"""
Problem:  Textwrap the string with the Given  max_width

Sample Input : ABCDEFGHIJKLIMNOQRSTUVWXYZ
               4

Platform: HackerRank

Difficulty: Mid

"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string , max_width)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)