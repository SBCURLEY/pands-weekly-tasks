# collatz.py
# This program asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.
# Author: Sharon Curley

endNumber = 1

number = int(input("Please enter a positive integer:")) 

while number != endNumber:                              # if the number is not equal to 1
    print(number)                                       # print the number
    if (number % 2) == 0:                               # if the number can be divided by 2 and equal zero - it is an even number (from pands-mywork-)
        number=(number//2)                              # Proceed to divide by 2

    else: number=((3*number)+1)                         # if the number cannot be divided by 2 and equal zero, apply 3x=1
                                                        # As there are only two conditions we use If..Else. If there were further conditions we would use If, Elif & Else.
                                                        # Loop continues
                                                        
print (endNumber)                                       # loop ends when the result is equal to endNumber (1)

# References: 
# Python Pool:          https://www.pythonpool.com/collatz-sequence-python/
# Youtube video on The Collatz Conjecture      https://www.youtube.com/watch?v=094y1Z2wpJg&t=1       Enter 341 as Integer
# Python If...Else      https://www.w3schools.com/python/python_conditions.asp
# lab04.01.01-isEven.py Even Number