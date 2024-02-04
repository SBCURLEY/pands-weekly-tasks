# bank.py
# This program will print out the sum of two Euro Values
# Author Sharon Curley

Amount1 = int (input ("\nEnter Amount 1 (in cent): "))
Amount2 = int (input ("Enter Amount 2 (in cent): "))
answer =  (Amount1 + Amount2)/100
print (f"\nThe sum of Amount 1 and Amount 2 is €{answer}.\n")
