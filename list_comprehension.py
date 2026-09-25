

"""
Problem:  Obtain the marks greater than or equal to 90 using list comprehension

Platform : SelfStudy

Difficulty: Mid

"""


marks = [45 , 90 , 63 , 99 , 69]

above_90 =list(filter(lambda mark : mark >= 90 , marks))
print(above_90)