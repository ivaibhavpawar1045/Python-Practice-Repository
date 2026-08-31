
"""
Problem:  This problem asks you to calculate final happiness by scanning the array:

          Add +1 if an element belongs to set A.

          Add -1 if an element belongs to set B.

          Add 0 otherwise.

Sample Input : User define

Platform: HackerRank

Difficulty: Mid

"""

n, m = map(int, input().split())

arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for value in arr:
    if value in A:
        happiness += 1
    elif value in B:
        happiness -= 1

print(happiness)