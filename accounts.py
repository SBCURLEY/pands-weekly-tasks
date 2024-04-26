# accounts.py
# This program reads in a 10 character account number and outputs the account number with only the last 4 digits showing
# Author: Sharon Curley

accountno = input("Please enter a 10 digit account number: ")

# print (accountno[6:])                     # test print the last 4 digits as passes over 6. Comments out
# print (accountno[:4])                     # test prints the first 4 digits

accountnoX ="xxxxxx"+str(accountno[6:])     # Substitutes 6 digits from the left with "xxxxxx"

print (accountnoX)                          # prints the number as follows xxxxxx4568


# References
# Real Python       https://realpython.com/python-input-output/
# Stack Overflow    https://stackoverflow.com/questions/63791824/how-to-print-the-last-two-digits-of-a-4-digit-input-taken-by-the-user
