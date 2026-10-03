
"""
Problem:  Vincent works in a door mat manufacturing company. One day, he designed a new door mat

Platform : HackerRank

Difficulty: Mid

"""

n, m = map(int, input().split())

# Top half
for i in range(1, n // 2 + 1):
    pattern = ".|." * (2 * i - 1)
    print(pattern.center(m, "-"))

# Middle line
print("WELCOME".center(m, "-"))

# Bottom half
for i in range(n // 2, 0, -1):
    pattern = ".|." * (2 * i - 1)
    print(pattern.center(m, "-"))