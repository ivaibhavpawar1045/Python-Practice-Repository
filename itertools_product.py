"""
Problem:  You are given a two lists A  and B . Your task is to compute their cartesian product X * Y.

Platform : HackerRank

Difficulty: Mid

"""


from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A, B))