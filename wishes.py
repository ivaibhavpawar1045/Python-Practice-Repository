

"""
Problem:  Wirte the present time and computer give the wishes .

Sample Input : User given

Platform: Self study
Difficulty: Easy 

"""

import time
t= time.strftime('%H:%M:%S')
hour = int(input("Enter Your Time : "))     # for taking time from user
print(t)

if hour < 12:
     print("Good Morning Sir!")
elif hour < 18:
     print("Good Afternoon Sir !")
elif hour < 24:
     print("Good Evening Sir !")