"""
Problem:  If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list.
           The delimiter is space (ascii 32) by default. 
          To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter.

Platform : HackerRank

Difficulty: Mid

"""


numbers = list(map(int, input().split()))
print(numbers)