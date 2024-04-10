# plottask.py
# author: Monika Dabrowska
# Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, 


import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(5, 2, 1000)

# Plot histogram of the normal distribution
plt.hist(data, alpha=0.9, color='blue', label='Normal Distribution', edgecolor="black")

# Generate x values for the function h(x) = x^3
x = np.linspace(0, 10, 100)
y = x ** 3

# Plot the function h(x) = x^3
plt.plot(x, y, color='green', label='$h(x) = x^3$')

# Add legend, labels, and title
plt.legend()
plt.xlabel('Values')
plt.ylabel('Frequency / $h(x)$')
plt.title('Histogram of Normal Distribution and Plot of $h(x) = x^3$')
plt.show()


# https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/

