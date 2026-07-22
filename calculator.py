
"""
Problem:  Make the easy calculator which takes the input from the user. 
          Performs the arithmatic operations.

Sample Input : Given by user

Platform: Self study
Difficulty: Easy 

"""

a = int(input("Enter your First Number : "))
b = int(input("Enter your Second Number : "))
c = input("Choose the operator { + , - , * , / } : ")

if c == '+':
     print(f"The Addition of {a} and {b} is   :  { a + b } " )
elif c == '-':
     print(f"The Substraction of {a} and {b} is   :  { a - b }  ")
elif c == '*':
     print(f"The Multiplication of {a} and {b} is   :  { a * b }  ")
elif c == '/':
     print(f"The Division of {a} and {b} is   :  { a / b } " )
else:
     print(" Please enter the valid input......!")