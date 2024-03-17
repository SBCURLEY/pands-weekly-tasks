# accounts2.py
# This program reads in account numbers of any length and outputs the account number with only the last 4 digits showing
# Author: Sharon Curley

accountno = input("Please enter an account number: ")

accountnox = accountno[-4:].rjust(len(accountno),'x')           # rjust() will right-justify the string within spaces of a given length. 
                                                                # As we do not know the length of the spaces required, we need to count the number using the len function on accountno
                                                                # The program will count the number of digits and replace with x

print (accountnox)


# References:
# A Whirlwind Tour of Python - Formatting strings: Adding and removing space P.71
# W3 Schools        https://www.w3schools.com/python/ref_string_rjust.asp
# A Whirlwind Tour of Python - String Type P.28
# W3 Schools        https://www.w3schools.com/python/python_strings.asp