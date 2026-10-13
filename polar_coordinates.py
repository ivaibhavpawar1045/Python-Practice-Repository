"""
Problem:  Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

Platform : SelfStudy

Difficulty: Mid

"""



import cmath

z = complex(input())

r, phi = cmath.polar(z)
print(r)
print(phi)