# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:29:46 2024

@author: angec
"""
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.cos(x)
plt.scatter(x, y)

f = interp1d(x, y, kind='cubic')

new_x = np.linspace(0, 10, 30)
result = f(new_x)

plt.scatter(x, y)
plt.scatter(new_x, result, c='r')

def f (x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

from scipy import optimize

params, params_cov = optimize.curve_fit(f, x, y)

plt.scatter(x, y)
plt.plot(x, f(x, params[0], params[1], params[2], params[3]), c='g', lw=3)
