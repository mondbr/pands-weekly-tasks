


import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(5, 2, 1000)

# Plot the histogram of the normal distribution
plt.hist(data, bins=30, density=True, alpha=0.5, color='blue', label='Normal Distribution')

# Generate values for the function h(x) = x^3
x = np.linspace(0, 10, 100)
y = x**3

# Plot the function h(x) = x^3
plt.plot(x, y, color='red', label='$h(x) = x^3$')

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Frequency / $h(x)$')
plt.title('Histogram of Normal Distribution and Plot of $h(x) = x^3$')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()