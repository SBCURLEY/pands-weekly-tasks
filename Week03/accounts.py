# accounts.py
# This program reads in a 10 character account number and outputs the account number with only the last 4 digits showing
# Author: Sharon Curley

accountno = input("Please enter a 10 digit account number: ")

                                            # print (accountno[6:])       # prints the last 4 digits as passes over 6
                                            # print (accountno[:4])     prints the first 4 digits

accountnoX ="xxxxxx"+str(accountno[6:])

print (accountnoX)


