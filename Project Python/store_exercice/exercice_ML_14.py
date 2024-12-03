# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:12:58 2024

@author: angec
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 20)
y = x**2

plt.figure()
plt.plot(x, y, label='quadratique')
plt.plot(x, x**3, label='cubique')
plt.title('figure 1')
plt.xlabel('axe x')
plt.ylabel('axe y')
plt.legend()

plt.savefig('figure.png')
plt.show()


plt.subplot(2, 1, 1)
plt.plot(x, y, c='red')
plt.subplot(2, 1, 2)
plt.plot(x, y, lw=2, ls='--',c='blue')


dataset = {f"experience{i}": np.random.randn(100) for i in range(4)}

def graphique_test(dataset): 
    L=[]
    for value in dataset.values():
        L.append(value)
    
    plt.figure(figsize=(10, 10))
    plt.subplot(4, 1, 1)
    plt.plot(np.linspace(0, 99, 100), L[0], label='unknown')
    plt.title('experience 1')
    plt.subplot(4, 1, 2)
    plt.plot(np.linspace(0, 99, 100), L[1], label='unknown')
    plt.title('experience 2')
    plt.subplot(4, 1, 3)
    plt.plot(np.linspace(0, 99, 100), L[2], label='unknown')
    plt.title('experience 3')
    plt.subplot(4, 1, 4)
    plt.plot(np.linspace(0, 99, 100), L[3], label='unknown')
    plt.title('experience 4')
    plt.xlabel('axe x')
    plt.ylabel('axe y')
    plt.legend()
    plt.show()
    return
        
def graphique_test2(data):
    n = len(data)
    plt.figure(figsize=(12, 12))
    x = np.linspace(0, 99, 100)
    i = 1
    for value in data.values():
        plt.subplot(n, 1, i)
        plt.plot(x, value, label='unknown')
        plt.title(f'experience{i}')
        i += 1
    plt.legend()
    plt.show()
    return

def graphique_correction(data):
    n = len(data)
    plt.figure(figsize=(12, 12))
    for k, i in zip(data.keys(), range(1, n+1)):
        plt.subplot(n, 1, i)
        plt.plot(data[k])
        plt.title(k)
    plt.show()
    return