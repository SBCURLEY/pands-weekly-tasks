# squareroot.py
# This program takes a positive floating-point number as input and outputs an approximation of its square root.
# This program will not use the built in functions 
# Author: Sharon Curley

# In algebra, a square, x, is the result of a number, n, multiplied by itself: x = n²

# x ** .5 ()  -  exponent operator                   Reference: https://realpython.com/python-square-root-function/
# math.sqrt(x). - predefined function that is defined in the math module.     # Reference: https://realpython.com/python-square-root-function/

# References (Newton): https://realpython.com/lessons/how-square-roots-are-calculated/
# References (Newton): Square Root of a Number using Newton's Method | Python | The Last Minute Professor      https://youtu.be/xdlIFw5EM4w

# An approx is made and a better value is determined based on the approx and then you keep doing that until you get the precision you desire.

# First attempt, I started without a function

''' 
num = float(input("Please Enter any Positive Number : "))  
approx=0.5*num                                                  # assume approx is half the number
better=0.5*(approx+num/approx)                                  # find a better value using Newtons method
while (better!=approx):                                         # while better found is not equal to the assumed approx
    approx = better                                             # assume the found better value as approx 
    better=0.5*(approx+num/approx)                              # recalculate better value using formula

print (f"The square root of {num} is approx. {better}")
'''

# Second attempt I created a function to recalculate better, I got it working but thought I could add more to the function

'''
def sqrt():
    better=0.5*(approx+num/approx)                              # recalculate better value using formula
    return better

num = float(input("Please Enter any Positive Number : "))  
approx=0.5*num                                                  # assume approx is half the number
better=0.5*(approx+num/approx)                                  # find a better value using Newtons method

while (better!=approx):                                         # while better found is not equal to the assumed approx
    approx = better                                             # assume the found better value as approx 
    better = sqrt()
    
print (f"The square root of {num} is approx. {better}")
'''

# Thirdly, I created a function to recalculate better & return it as approx. 

def sqrt():                                                     # define the function square root
    approx=0.5*num                                              # assume approx is half the number
    better=0.5*(approx+num/approx)                              # find a better value using Newtons method 
    while (better!=approx):                                     # while better found is not equal to the assumed approx
        approx = better                                         # assume the found better value as approx 
        better=0.5*(approx+num/approx)                          # recalculate better value using formula
    return approx                                               # return the new approx
                                                                # keep doing that until you get the result.

num = float(input("Please Enter any Positive Number : "))       # input a float

print (f"The square root of {num} is approx. {'%.1f' % sqrt()}")        # Print the answer to one decimal place
                                                                        # Reference for decimal places 
                                                                        # https://www.askpython.com/python/built-in-methods/format-2-decimal-places