
"""
Problem:   Given an integer, n , and n  space-separated integers as input,
          create a tuple,t , of those n  integers. Then compute and print the result of hash(t).

Sample Input : 2
               1 2

Platform: HackerRank
Difficulty: Easy 

"""

n = int(input())
t = tuple(map(int , input().split()))
print(hash(t))