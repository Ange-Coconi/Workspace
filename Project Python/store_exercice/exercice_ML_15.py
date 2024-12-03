# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:19:58 2024

@author: angec
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data
y = iris.target
names = list(iris.target_names)

print(f'x contient {x.shape[0]} exemples et {x.shape[1]} variables')
print(f'il y a {np.unique(y).size} classes')

def graphique(data):
    n = x.shape[1]
    plt.figure(figsize=(12, 15))
    for i in range(n):
        plt.subplot(n, 1, i+1)
        plt.plot(x[:, i])
    plt.show()
    return

def graphique_2(x, y):
    plt.figure(figsize=(12, 15))
    L = []
    for z in set(y):
        L.append(z)
        G = []
        for i in range(x.shape[0]):
            if y[i] == L[z]:
                G.append(x[i, :])
        plt.subplot(len(set(y)), 1, z+1)
        plt.plot(G)        
    plt.show()
    return

# Correction
classes = list(np.unique(y))
print(classes)

n = x.shape[1]
plt.figure(figsize=(12, 8))
for i in range(n):
    plt.subplot(n//2, n//2, i+1)
    plt.scatter(x[:, 0], x[:, i], c=y)
    plt.xlabel('0')
    plt.ylabel(i)
    plt.colorbar(ticks=np.unique(y))
plt.show()

print(graphique_2(x, y))