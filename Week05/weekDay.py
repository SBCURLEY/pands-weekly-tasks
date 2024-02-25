# weekDay.py
# This program will output whether or not today is a weekday
# Author: Sharon Curley.

import datetime         
# Import the datetime module to display the current date.
# Reference: Python Dates (w3schools.com)

date = datetime.datetime.now()

# When we execute the code from the example above the result will be:  2024-02-25 05:52:33.388577

# print(date)
# Test it out - all ok - now comment out the print of date

# From the above date, we need to pull out the day of the week
# # Reference: Python Dates (w3schools.com) - A reference of all the legal format codes available to us on W3 Schools
# %A is the one required for this code as it is Weekday (full version) e.g. Wednesday

today = (date.strftime("%A"))

# print (weekday)
# Test it out - all ok - now comment out the print of weekday

# Define what days of the week are weekdays using a Tuple
# References: https://realpython.com/python-lists-tuples/
# Q: Why choose Tuple over List?  References: A Whirlwind Tour Of Python 2 Jake VanderPlas  Page 31
# Lists are the basic ordered and mutable data collection type in Python.
# Tuples are in many ways similar to lists, but they are defined with parentheses rather than square brackets
# The main distinguishing feature of tuples is that they are immutable: this means that once they are created, their size and contents cannot be changed:
# WeekDays is not going to change so I went with Tuple

weekDays =(
    "Monday",               # 0    indexed
    "Tuesday",              # 1
    "Wednesday",            # 2
    "Thursday",             # 3
    "Friday",               # 4
    "Saturday",             # 5
    "Sunday"                # 6
)

# Check if today is a weekday (0 to 4) and if true, print "Yes, unfortunately today is a weekday.""
# Reference: lab05.02-months.py - this example used months in a Tuple.

if today == [0-4]:
    print ("Yes, unfortunately today is a weekday.")

# Otherwise print It is the weekend, yay!  
else:
    print ("It is the weekend, yay!")

