"""
Problem:  The calendar module allows you to output calendars and provides additional useful functions for them.

Platform : HackerRank

Difficulty: Mid

"""

import calendar

cal = calendar.TextCalendar(firstweekday=6)
print(cal.formatmonth(2026, 10))