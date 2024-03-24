<h1 align="center">Pands Weekly Tasks</h1>

## Description
The following will summarise all of the weekly tasks for the Programming and Scripting Module

## Table of Contents
- Topic 01 - Set Up
- Topic 02 - Statements
- Topic 03 - State (Variables)
- Topic 04 - Controlling the Flow 
- Topic 05 - Data structures
- Topic 06 - Functions
- Topic 07 - Files
- Topic 08 - Plotting data

## Git Hub Repository Links

- Topic 01 - (https://github.com/SBCURLEY/pands-weekly-tasks/tree/main/Week01)
- Topic 02 - (https://github.com/SBCURLEY/pands-weekly-tasks/tree/main/Week02)
- Topic 03 - (https://github.com/SBCURLEY/pands-weekly-tasks/tree/main/Week03)
- Topic 04 - (https://github.com/SBCURLEY/pands-weekly-tasks/tree/main/Week04)
- Topic 05 - (https://github.com/SBCURLEY/pands-weekly-tasks/tree/main/Week05)
- Topic 06 - (https://github.com/SBCURLEY/pands-weekly-tasks/tree/main/Week06)
- Topic 07 - (https://github.com/SBCURLEY/pands-weekly-tasks/tree/main/Week07)
- Topic 08 - (https://github.com/SBCURLEY/pands-weekly-tasks/tree/main/Week08)

## Description of Topics

**Topic 01 - Set Up**
Commit and push a file to the weekly tasks repository called ''helloworld.py
The file contains a python program that displays Hello World! when it is run.


**Topic 02 - Statements**
This program is called 'bank.py'. It prompts the user and reads in two money amounts (in cent), .e.g. 55.
It adds the two amounts. It prints out the the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. e.g €1.20cd


# Topic 03 - State (Variables)
There are two programs for this topic -'accounts.py' and 'accounts2.py' The 'accounts.py' program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs). The second program called 'accounts2.py' modify the accounts.py program to deal with account numbers of any length. It will only print the last four  - all before will be replaced with an x.


# Topic 04 - Controlling the Flow 
The 'collatz.py' program asks the user to input any positive integer. It then outputs the successive values of the following calculation.
At each step it calculates the next value by taking the current value and if it is even, divide it by two, but if it is odd, multiply it by three and add one.
When the program reaches zero, it ends.


# Topic 05 - Data structures
The 'weekDay.py' program outputs whether whether or not today is a weekday. If it runs on a weekday it will output 'Yes, unfortunately today is a weekday.'
If it is a weekend, it will output 'It is the weekend, yay!'.


# Topic 06 - Functions
The 'squareroot.py' program takes a positive floating-point number as input and outputs an approximation of its square root.
This program will not use the built in functions, e.g.math.sqrt(x). A deep dive into Newton theory was required.
The Newton theory in a nutshell is let N be any number then the square root of N can be given by the formula: root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
An approx is made and a better value is determined based on the approx and then you keep doing that until you get the precision you desire.


# Topic 07 - Files
The 'es.py' program reads in a text file and outputs the number of e's it contains. The program takes the filename from an argument on the command line.
As an example, python .\es.py "moby-dick.txt" will count the number of e's in the text file "moby-dick.txt". 
On the other hand, python .\es.py "test.txt" will count the number of e's in "test.txt", but there are no e's in that file. The program will return 'There is no e in this txt file'.


## Topic 08 - Plotting data

The program 'plottask.py' plots a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
Additionally it plots the function  h(x)=x3 in the range 0 to 10 on the one set of axes. The Histogram is saved as a file. 


## Built With
Python


## Author
- Sharon Curley
- [Profile](https://github.com/SBCURLEY "Sharon Curley")
- [Email](mailto:sbrogancurley@gmail.com?subject=Hi% "Hi!")
