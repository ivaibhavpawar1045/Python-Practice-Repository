"""
Problem:  You are given two values , handle the exception

Platform : HackerRank

Difficulty: Mid
"""


t = int(input())

for _ in range(t):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)