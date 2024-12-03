# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:41:58 2024

@author: angec
"""
import numpy as np



np.random.seed(0)
A = np.random.randint(0, 100, [10, 5])

# Methode 1
B = np.ones([10, 5])
for colonne in range(A.shape[1]):
    M = np.mean(A[:,colonne])
    O = np.std(A[:,colonne])
    for ligne in range(A.shape[0]):
        B[ligne, colonne] = (A[ligne, colonne] - M) / O
    
print(B)


# Methode 2
D = (A - A.mean(axis=0)) / A.std(axis=0)

print(D)


# Methode 3
np.random.seed(0)
C = np.random.randint(0, 100, [10, 5]).astype(float)

for colonne in range(C.shape[1]):
    M2 = np.mean(C[:,colonne])
    O2 = np.std(C[:,colonne])
    for ligne in range(C.shape[0]):
        C[ligne, colonne] = (C[ligne, colonne] - M2) / O2
    
print(C)
