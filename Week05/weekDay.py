# weekDay.py
# This program will output whether or not today is a weekday
# Author: Sharon Curley.

import datetime                                             # Import the datetime module to display the current date.  

date = datetime.datetime.now()                              # When we execute the code from the example above the result will be:  2024-02-25 05:52:33.388577

# print(date)                                               # Test it out - all ok - now comment out the print of date
                                                            # From the above date, we need to pull out the day of the week
                                                            
today = (date.strftime("%A"))                               # This will convert a datetime object containing current date and time to different string formats.
                                                            # We use %A for this code as it is Weekday (full version) e.g. Wednesday

# print (weekday)                                           # Test it out - all ok - now comment out the print of weekday

                                                            # Question for myself: Why choose Tuple over List?  
                                                            # Lists are the basic ordered and mutable data collection type in Python.
                                                            # Tuples are in many ways similar to lists, but they are defined with parentheses rather than square brackets
                                                            # The main distinguishing feature of tuples is that they are immutable: 
                                                            # this means that once they are created, their size and contents cannot be changed:
                                                            # WeekDays is not going to change so I went with Tuple

weekDays =(                                                 # Define what days of the week are weekdays using a Tuple
    "Monday",                                               # 0    indexed
    "Tuesday",                                              # 1
    "Wednesday",                                            # 2
    "Thursday",                                             # 3
    "Friday",                                               # 4
    "Saturday",                                             # 5
    "Sunday"                                                # 6
)

if today == [0-4]:                                          # Check if today is a weekday (0 to 4) 
    print ("Yes, unfortunately today is a weekday.")        # and if true, print "Yes, unfortunately today is a weekday."

else:                                                       # Otherwise print It is the weekend, yay!  
    print ("It is the weekend, yay!")
    
    
# References
# W3 Schools        https://www.w3schools.com/python/python_datetime.asp
# Geeks for Geeks   https://www.geeksforgeeks.org/python-strftime-function/
# Real Python       https://realpython.com/python-lists-tuples/
# A Whirlwind Tour Of Python 2 Jake VanderPlas  Page 31    Why choose Tuple over List?  
# lab05.02-months.py - this example used months in a Tuple.