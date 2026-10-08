"""
Problem:  Fibonacci recursion finds the nth Fibonacci number

Platform : SelfStudy

Difficulty: Mid

"""

def fibonacci(n):
     if n == 0 or n == 1 :
          return n

     return fibonacci(n-1) + fibonacci(n-2)


n = int(input())
print(fibonacci(n))