# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:22:37 2024

@author: angec
"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Generate a random sample of 1000 values from a normal distribution
mu = 0 # Mean
sigma = 1 # Standard deviation
sample = np.random.normal(mu, sigma, 1000)

# Calculate the PDF for the normal distribution
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
pdf = norm.pdf(x, mu, sigma)
# Plot the histogram of the random sample and the PDF of the normal distribution
plt.figure(figsize=(7.5, 3.5))
plt.hist(sample, bins=60, density=True, alpha=0.5)
plt.plot(x, pdf)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Generate a skewed distribution using NumPy's random function
data = np.random.gamma(2, 1, 1000)

# Plot a histogram of the data to visualize the distribution
plt.figure(figsize=(7.5, 3.5))
plt.hist(data, bins=30)

# Add labels and title to the plot
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Skewed Distribution')

# Show the plot
plt.show()