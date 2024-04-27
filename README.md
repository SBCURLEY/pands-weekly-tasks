<h1 align="center">Higher Diploma in Science in Computing (Data Analytics)</h1>
<h1 align="center">Programming and Scripting</h1>

# Description
The following will summarise all of the weekly tasks for the Programming and Scripting Module

# Table of Contents
1. Git Hub Repository Links
2. Description of Topics
3. Built With
4. About Author
5. References


# 1. Git Hub Repository Links

- Topic 01 - [helloworld.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/helloworld.py)
- Topic 02 - [bank.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/bank.py)
- Topic 03 - [accounts.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/accounts.py)
             [accounts2.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/accounts2.py)
- Topic 04 - [collatz.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/collatz.py)
- Topic 05 - [weekDay.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/weekDay.py)
- Topic 06 - [squareroot.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/squareroot.py)
- Topic 07 - [es.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/es.py)
             [moby-dick.txt](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/moby-dick.txt)
             [test.txt: error handling](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/test.txt)
- Topic 08 - [plottask.py](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/plottask.py)
             [Normal Distribution Histogram](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/Normal%20Distribution%20Histogram.png)

# 2. Description of Topics


## Topic 01 - Set Up
Commit and push a file to the weekly tasks repository called 'helloworld.py'.
The file contains a python program that displays Hello World! when it is run.

### Program & Sample Data
- $ python helloworld.py
- Hello World



## Topic 02 - Statements
This program is called 'bank.py'. It prompts the user and reads in two money amounts (in cent), .e.g. 55.
It adds the two amounts. It prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. e.g. €1.20

### Program & Sample Data
- $ python bank.py
- Enter amount1(in cent): 65
- Enter amount2(in cent): 180
- The sum of these is €2.45

### References
- Python Guides     https://pythonguides.com/python-print-2-decimal-places/ 
- w3schools.com     https://www.w3schools.com/python/python_variables.asp          Python Variables
- Real Python       https://realpython.com/python-f-strings/



## Topic 03 - State (Variables)
There are two programs for this topic -'accounts.py' and 'accounts2.py' The 'accounts.py' program reads in a 10-character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs). The second program called 'accounts2.py' modify the accounts.py program to deal with account numbers of any length. It will only print the last four  - all before will be replaced with an x.

### Program & Sample Data
- $ python accounts.py
- Please enter an 10 digit account number: 1234567890
- XXXXXX7890

- $ python accounts2.py
- Please enter an account number: 1234567891234567890
- XXXXXXXXXXXXXXX7890

### References
- Real Python       https://realpython.com/python-input-output/
- Stack Overflow    https://stackoverflow.com/questions/63791824/how-to-print-the-last-two-digits-of-a-4-digit-input-taken-by-the-user
- A Whirlwind Tour of Python - Formatting strings: Adding and removing space P.71
- W3 Schools        https://www.w3schools.com/python/ref_string_rjust.asp
- A Whirlwind Tour of Python - String Type P.28
- W3 Schools        https://www.w3schools.com/python/python_strings.asp



## Topic 04 - Controlling the Flow 
The 'collatz.py' program asks the user to input any positive integer. It then outputs the successive values of the following calculation.
At each step it calculates the next value by taking the current value and if it is even, divide it by two, but if it is odd, multiply it by three and add one.
When the program reaches zero, it ends.

### Program & Sample Data
- $ python collatz.py
- Please enter a positive integer: 10
- 10 5 16 8 4 2 1

### References
- Python Pool:          https://www.pythonpool.com/collatz-sequence-python/
- Youtube video on The Collatz Conjecture      https://www.youtube.com/watch?v=094y1Z2wpJg&t=1       Enter 341 as Integer
- Python If...Else      https://www.w3schools.com/python/python_conditions.asp
- lab04.01.01-isEven.py Even Number



## Topic 05 - Data structures
The 'weekDay.py' program outputs whether or not today is a weekday. If it runs on a weekday it will output 'Yes, unfortunately today is a weekday.'
If it is a weekend, it will output 'It is the weekend, yay!'.

### Program & Sample Data
This example is run on a Thursday
- $ python weekDay.py
- Yes, unfortunately today is a weekday.

### Program & Sample Data
This example is run on a Saturday
- $ python weekDay.py  
- It is the weekend, yay!

### References
- W3 Schools        https://www.w3schools.com/python/python_datetime.asp
- Geeks for Geeks   https://www.geeksforgeeks.org/python-strftime-function/
- Real Python       https://realpython.com/python-lists-tuples/
- A Whirlwind Tour Of Python 2 Jake VanderPlas  Page 31    Why choose Tuple over List?  
- lab05.02-months.py - this example used months in a Tuple.



## Topic 06 - Functions
The 'squareroot.py' program takes a positive floating-point number as input and outputs an approximation of its square root.
This program will not use the built in functions, e.g. math.sqrt(x). A deep dive into Newton theory was required.
The Newton theory in a nutshell is let N be any number then the square root of N can be given by the formula: root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
An approx. is made and a better value is determined based on the approx and then you keep doing that until you get the precision you desire.

### Program & Sample Data
- $ python squareroot.py
- Please enter a positive number: 14.5
- The square root of 14.5 is approx. 3.8.



### References
- Real Python:          https://realpython.com/python-square-root-function/
- Real Python Newton:   https://realpython.com/lessons/how-square-roots-are-calculated/
- Geeks for Geeks       https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
- Newton: Square Root of a Number using Newton's Method | Python | The Last Minute Professor      https://youtu.be/xdlIFw5EM4w
- Ask Python             https://www.askpython.com/python/built-in-methods/format-2-decimal-places



## Topic 07 - Files
The 'es.py' program reads in a text file and outputs the number of e's it contains. The program takes the filename from an argument on the command line.
As an example, python .\es.py "moby-dick.txt" will count the number of e's in the text file "moby-dick.txt". 
On the other hand to incorporate error handling, python .\es.py "test.txt" will count the number of e's in "test.txt", but there are no e's in that file. The program will return 'There is no e in this txt file'.

### Program & Sample Data
- $ python es.py moby-dick.txt
- 101

### Program & Sample Data
- $ python es.py test.txt
- There is no e in this txt file

### References
- Python            https://docs.python.org/3/library/sys.html 
- Real Python       https://realpython.com/python-command-line-arguments/
- Free code camp    https://www.freecodecamp.org/news/if-name-main-python-example  (if __name__ == "__main__":)  
- Machine Learning Tutorials    https://machinelearningtutorials.org/understanding-if-__name__-__main__-in-python-with-examples/ 
- Geeks for Geeks   https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/   
- Real Python       https://realpython.com/lessons/sysargv-in-depth/
- Geeks for Geeks   https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
- Stack Overflow    https://stackoverflow.com/questions/4117530/what-does-sys-argv1-mean-what-is-sys-argv-and-where-does-it-come-from
- Stack Overflow    https://stackoverflow.com/questions/36026798/counting-letters-in-a-text-file-in-python
- W3 Schools        https://www.w3schools.com/python/python_file_open.asp
- Real Python       https://realpython.com/read-write-files-python/
- GitHub            https://eldoyle.github.io/PythonIntro/08-ReadingandWritingTextFiles/



## Topic 08 - Plotting data

The program 'plottask.py' plots a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
Additionally it plots the function  h(x)=x3 in the range 0 to 10 on the one set of axes. The Histogram is saved as a file.

### Program & Sample Data
- $ python plottask.py
- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
- and a plot of the function  h(x)=x3 in the range 0 to 10
- on the one set of axes.
[Normal Distribution Histogram.png](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/Week08/Normal%20Distribution%20Histogram.png/)

![Normal Distribution Histogram.png](https://github.com/SBCURLEY/pands-weekly-tasks/blob/main/Week08/Normal%20Distribution%20Histogram.png/)

### References
- Numpy.org             https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
- Real Python           https://realpython.com/python-histograms/
- Datacamp              https://www.datacamp.com/tutorial/histograms-matplotlib
- Matplotlib            https://matplotlib.org/stable/gallery/statistics/hist.html
- Statology             https://www.statology.org/matplotlib-histogram-color/
- Python Graph Gallery  https://python-graph-gallery.com/190-custom-matplotlib-title/
- Datagy                https://datagy.io/matplotlib-title/
- matplotlib.org        https://matplotlib.org/stable/users/explain/text/index.html
- Week08 - messingWithMathplotlib
- Pythonspot            https://pythonspot.com/matplotlib-legend/



## 3. Built With
- Python 
- Visual Studio Code
- Cmder



## 4. About Author
- Sharon Curley
- [Profile](https://github.com/SBCURLEY "Sharon Curley")
- [Email](mailto:sbrogancurley@gmail.com?subject=Hi% "Hi!")



## 5. References
 - https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
 - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
 - https://dev.to/rohit19060/how-to-write-stunning-github-readme-md-template-provided-5b09
