"""
Problem:  You are given a date. Your task is to find what the day is on that date.

Platform : HackerRank

Difficulty: Mid

"""

import calendar
import datetime

month, day, year = map(int, input().split())

d = datetime.date(year, month, day)
print(calendar.day_name[d.weekday()].upper())