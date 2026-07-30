
"""
Problem:  Complete the swap_case function in the editor below.

          swap_case has the following parameters:

          string s: the string to modify

Sample Input : HackerRank.com presents "Pythonist 2".

Platform: HackerRank

Difficulty: Easy 

"""

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)