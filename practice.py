"""
Problem:  Use the lambda function to find the number is even or odd

Sample Input : User define

Platform: SelfStudy

Difficulty: easy

"""


a = int(input("Enter your Number : "))
num = lambda a : "Even Number" if a % 2 == 0 else "Odd Number"
print(num(a))