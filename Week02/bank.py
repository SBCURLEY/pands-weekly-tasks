# bank.py
# This program will print out the sum of two Euro Values
# Author Sharon Curley

Amount1 = int (input ("\nEnter Amount 1 (in cent): "))              # Use \n to create a space before the two inout lines.
Amount2 = int (input ("Enter Amount 2 (in cent): "))                # Line 5 and 6  require the function int before input as the program will see it as a string if not included. 
answer = float (Amount1 + Amount2)/100                              # This is an integer & must be changed to a float by using = float.
answerFloat="{:.2f}".format(answer)                                 # to print 2 decimal places, use str.format() with “{:.2f}” as string and float as a number. 

print (f"\nThe sum of Amount 1 and Amount 2 is €{answerFloat}.\n")  # Line 10 uses an f-string which contains a replacement field {answer} enclosed by curly brackets.  
                                                                    # Line 10 uses \n to create a space before and after the output.

# References:
# Python Guides     https://pythonguides.com/python-print-2-decimal-places/ 
# w3schools.com     https://www.w3schools.com/python/python_variables.asp          Python Variables
# Real Python       https://realpython.com/python-f-strings/