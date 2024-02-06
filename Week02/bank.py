# bank.py
# This program will print out the sum of two Euro Values
# Author Sharon Curley

Amount1 = int (input ("\nEnter Amount 1 (in cent): "))
Amount2 = int (input ("Enter Amount 2 (in cent): "))
# Line 5 uses \n to create a space before the two inout lines.
# Line 5 and 6  require the function int before input as the program will see it as a string if not included. 
answer = float (Amount1 + Amount2)/100
# Line 9 is an integer & must be changed to a float by using = float. (Reference: w3schools.com - Python Variables - https://www.w3schools.com/python/python_variables.asp)
print (f"\nThe sum of Amount 1 and Amount 2 is €{answer}.\n")
# Line 11 uses an f-string which contains a replacement field {answer} enclosed by curly brackets.  Reference: Real Python - https://realpython.com/python-f-strings/
# Line 11 uses \n to create a space before and after the output.