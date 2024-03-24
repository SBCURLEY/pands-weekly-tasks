# plottask.py
# This program will plot
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function  h(x)=x3 in the range 0 to 10
# on the one set of axes.
# Author: Sharon Curley

import numpy as np 
import matplotlib.pyplot as plt 

normData = np.random.normal(loc=5, scale=2, size=1000)      # Plotting the histogram of gaussian (normal) distribution, which will have a mean of 5 and a standard deviation of 2
xpoints = np.array (range(1,11))                            # Create a plot in the range 1-10
ypoints = xpoints * xpoints * xpoints                       # function = h(x)=x3 

# print (normData)                                          # Validate the data and then comment out

# print (normData.mean(), normData.std())                   # Verify the mean and standard deviation, then comment out (5.077624952319204 1.9620082678644233)

plt.figure(figsize=[8,6])                                   # This sets the size of the figure to be displayed.

plt.xlabel("Value",                                         # Sets the label for the x-axis
fontsize=13,                                                # font size = controls the size of the font and sets it to 15
style="italic",                                             # style = controls the style of the font - italic
family="monospace")                                         # family = controls the font family of the font - monospace                       

plt.ylabel("Frequency",                                     # Sets the label for the y-axis
fontsize=13,                                                # font size = controls the size of the font and sets it to 15
style="italic",                                             # style = controls the style of the font - italic
family="monospace")                                         # family = controls the font family of the font - monospace.

plt.xticks(fontsize=10)                                     # Sets the font size of the x-axis tick labels to 10.
plt.yticks(fontsize=10)                                     # Sets the font size of the y-axis tick labels to 10.

plt.title ("Normal Distribution Histogram \nwith function h(x)=x3",                 # Sets the title name
fontsize=18,                                                # font size = controls the size of the font and sets it to 18.
loc="center",                                               # loc = The location of the title can be ‘center’, ‘left’, ‘right’.
horizontalalignment="center",                               # You can adjust with horizontal alignment ('center', 'right', 'left').
verticalalignment="bottom",                                 # the vertical alignment ('top', 'bottom', 'center', 'baseline')
fontweight="bold",                                          # font weight = controls the weight of the font - bold                      
family="monospace")                                         # family = controls the font family of the font - monospace

plt.grid(axis='y', alpha=0.75)                              # Set a grid with transparency of 0.75

plt.text(9, 620, r'$h(x)=x3$')                              # to show a formula on the graph

plt.hist(normData,                                          # plot normData
ec = "black",                                               # The ec (edge color) parameter define an edge on each bar with black outline.
lw = 1.75,                                                  # The lw (line width) can be increased
color ="#607c8e",                                           # The color parameter sets the color of the bars in the histogram.
alpha = 0.9,                                                # The alpha parameter sets the transparency of the bars.
rwidth= 0.85,                                               # rwidth sets the relative width of the bars as a fraction of the bin width.
label="Distribution")                                       # set label for histogram       

plt.plot (xpoints, ypoints, color="red", label="Function")  # plot the line and set color to red & label.
plt.legend(loc="center left")                               # show legend, location options are 'best', 
                                                            # 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 
                                                            # 'center right', 'lower center', 'upper center', 'center'
plt.savefig("Normal Distribution Histogram")                # save the Figure in Folder
plt.show ()                                                 # Displays the plot                





# References:   
# Numpy.org             https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# Real Python           https://realpython.com/python-histograms/
# Datacamp              https://www.datacamp.com/tutorial/histograms-matplotlib
# Matplotlib            https://matplotlib.org/stable/gallery/statistics/hist.html
# Statology             https://www.statology.org/matplotlib-histogram-color/
# Python Graph Gallery  https://python-graph-gallery.com/190-custom-matplotlib-title/
# Datagy                https://datagy.io/matplotlib-title/
# matplotlib.org        https://matplotlib.org/stable/users/explain/text/index.html
# Week08 - messingWithMathplotlib
# Pythonspot            https://pythonspot.com/matplotlib-legend/