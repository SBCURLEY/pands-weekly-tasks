# es.py
# Write a program that reads in a text file and outputs the number of e's it contains. 
# Author: Sharon Curley


# Firstly check if the file exists
# Referencees
# W3 Schools https://www.w3schools.com/python/python_file_open.asp
# Real Python  https://realpython.com/read-write-files-python/
# Stack Overflow https://stackoverflow.com/questions/36026798/counting-letters-in-a-text-file-in-python
# Geeks for Geeks  https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# GitHub https://eldoyle.github.io/PythonIntro/08-ReadingandWritingTextFiles/


import sys                                      # Reference https://realpython.com/python-command-line-arguments/
                                                # This module provides access to some variables used or maintained by the Python Command Line

if __name__ == "__main__":                      # https://www.freecodecamp.org/news/if-name-main-python-example/
                                                # https://machinelearningtutorials.org/understanding-if-__name__-__main__-in-python-with-examples/
                                                # https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
                                                
# print(f"Arguments count: {len(sys.argv)}")    # test print number of arguments (0,1)

    for i, arg in enumerate(sys.argv):          # Reference vhttps://docs.python.org/3/library/sys.html   
        i=1                                     # The list of command line arguments passed to a Python script. argv[0] is the script name 
                                                # i = 1 is the file name passed in after python command. (es.py = arg0)
#print(f"{arg}")                               # test print list the argument, e.g. moby-dick.txt

import os.path                              # to check if the file exists
FILENAME = (f"{arg}")                       # filename is pulled from argument1 above
if not os.path.isfile(FILENAME):            # If file does not exist, print message and end program
    print("File does not exist")            
else:                                       # if argument1 exists (FILENAME), count letters
    def letterFrequency (FILENAME, letter):
        with open (FILENAME, 'r') as f:         # The file is opened using the open() function in the read mode. Teh with open will automatically close.
            text = f.read()                     # store content of the file in a variable
            count = 0                           # declare count variable as we need to count letters

        for char in text:                       # A for loop is used to read through each line in the file.
            if char == letter:                  # compare each character with the given letter in the print command
                count += 1                      # count each character
        return count                            # return letter count of given letter
    

#print(letterFrequency(FILENAME, "e"))          # print the number of e's. But what if there was no e.

if (letterFrequency(FILENAME, "e"))>0:             # if there is more than one e in the file it will
    print(letterFrequency(FILENAME, "e"))        # print the number of e's
else:                                           # if not
    print("There is no e in this txt file")     # print that they do not exist.