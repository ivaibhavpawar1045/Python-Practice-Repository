"""
Problem:  A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Platform : HackerRank

Difficulty: Mid

"""



from collections import Counter

x = int(input())
sizes = Counter(map(int, input().split()))

n = int(input())
money = 0

for _ in range(n):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        money += price
        sizes[size] -= 1

print(money)