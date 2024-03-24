# es.py
# Write a program that reads in a text file and outputs the number of e's it contains. 
# Author: Sharon Curley


import sys                                      # This module provides access to some variables used or maintained by the interpreter 
                                                # and to functions that interact strongly with the interpreter. 
if __name__ == "__main__":                      # When the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
                                                # But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.
                                                # The construct if __name__ == "__main__": is a conditional statement that checks if the script is being run as the main program.
                                                # It is, the code block under this statement is executed; otherwise, if the script is being imported as a module, the code block is not executed.

# print(f"Arguments count: {len(sys.argv)}")    # test print number of arguments. Comment out after.

    for i, arg in enumerate(sys.argv):          # For every invocation of Python, sys.argv is automatically a list of strings representing the arguments (as separated by spaces) on the command-line.
        i=1                                     # The list of command line arguments passed to a Python script. argv[0] is the script name
                                                # i = 1 is the file name passed in after python command. (es.py = arg0)
#   print(f"{arg}")                             # test print list the argument, e.g. "moby-dick.txt" = arg1. Comment out after.

import os.path                                  # to check if the file exists. (sys.argv has no built in error handling)
FILENAME = (f"{arg}")                           # filename is pulled from argument1 above
if not os.path.isfile(FILENAME):                # If file does not exist, print message and end program
    print("File does not exist")            
else:                                           
    def letterFrequency (FILENAME, letter):     # if argument1 exists (FILENAME), count letters
        with open (FILENAME, 'r') as f:         # The file is opened using the open() function in the read mode. The with open will automatically close.
            text = f.read()                     # store content of the file in a variable
            count = 0                           # declare count variable as we need to count letters

        for char in text:                       # A for loop is used to read through each line in the file.
            if char == letter:                  # compare each character with the given letter in the print command
                count += 1                      # count each character
        return count                            # return letter count of given letter
    

# print(letterFrequency(FILENAME, "e"))       # print the number of e's. But what if there was no e. I got an error. 
                                                # I created another text file "test.txt which does not contain any e's
                                                # I got an error.
                                                # Comment out and create an if statement

if (letterFrequency(FILENAME, "e"))>0:          # if there is more than one e in the file it will
    print(letterFrequency(FILENAME, "e"))       # print the number of e's
else:                                           # if not
    print("There is no e in this txt file")     # print that they do not exist.
    
    
    
    
    

# References
# Python            https://docs.python.org/3/library/sys.html 
# Real Python       https://realpython.com/python-command-line-arguments/
# Free code camp    https://www.freecodecamp.org/news/if-name-main-python-example  (if __name__ == "__main__":)  
# Machine Learning Tutorials    https://machinelearningtutorials.org/understanding-if-__name__-__main__-in-python-with-examples/ 
# Geeks for Geeks   https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/   
# Real Python       https://realpython.com/lessons/sysargv-in-depth/
# Geeks for Geeks   https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# Stack Overflow    https://stackoverflow.com/questions/4117530/what-does-sys-argv1-mean-what-is-sys-argv-and-where-does-it-come-from
# Stack Overflow    https://stackoverflow.com/questions/36026798/counting-letters-in-a-text-file-in-python
# W3 Schools        https://www.w3schools.com/python/python_file_open.asp
# Real Python       https://realpython.com/read-write-files-python/
# GitHub            https://eldoyle.github.io/PythonIntro/08-ReadingandWritingTextFiles/