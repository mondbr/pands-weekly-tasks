# plottask.py
# author: Monika Dabrowska
# Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, 


# this statement imports the NumPy library and assign as a shorter name 'np'
# thst can be used thorough the code. NumPy is a Python library used for numercal computing, array manipulation etc.
import numpy as np 

# this statement imports the pyplot module from the Matplotlib library and assigns it an plt.
# module allows creating plots, histograms and adding legends and titles to it.
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
# '5' specifies the mean of the normal distribution
# '2'  standard deviation of the normal distribution
# '1000' number of random values to generate. 
# I am assigning variable (dataset) 'data' of 1000 random numbers sampled from a normal distribution 
# with a mean of 5 and a standard deviation of 2 using NumPy.
data = np.random.normal(5, 2, 1000)


# Plot histogram of the normal distribution:
# creates a histogram plot of the data generated from the normal distribution using Matplotlib's hist() function.
# 'data' dataset I want to plot as a histogram
# 'alpha' parameter sets the transparency level of the histogram bars. A value of 0.1 means the bars 
# will be very transparent, allowing any underlying data or other elements of the plot to be visible through them
# 'color', 'label' amd 'edgecolor' are specifing color of the histogram bars, label to historgam plot and color of the edges of the histogram bars

plt.hist(data, alpha=0.1, color='blue', label='Normal Distribution', edgecolor="black")



# Generate x values and calculate corresponding y values for the function h(x) = x^3
# This line generates 100 equally spaced values between 0 and 10 inclusive using NumPy's linspace() function. 
# These values represent the x-coordinates for plotting the function
# and assign to variable x
x = np.linspace(0, 10, 100)

# This line calculates the corresponding y values for the function 
# by raising each x value to the power of 3.
y = x ** 3

# the above code means that 'x' will contain 100 x values evenly spaced between 0 and 10, 
# and 'y' will contain the corresponding y values calculated using the function h(x) = x^3 
# (y = x^3)

# Plot the function h(x) = x^3
plt.plot(x, y, color='green', label='$h(x) = x^3$')

# Add legend, labels, and title
plt.legend()
plt.xlabel('Values')
plt.ylabel('h(x) = x^3')
plt.title('Histogram of Normal Distribution and Plot of $h(x) = x^3$')

# print the histogram and plot
plt.show()


# https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
# lecture videos from Principles of Data analytics and Programming and scripting modules

