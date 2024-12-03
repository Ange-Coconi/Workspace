# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:32:41 2024

@author: angec
"""
import numpy as np

def initialisation(m,n):
    # m : nombre de lignes
    # n : nombre de colonnes
    # retourne une matrice aléatoire
    # avec une colonne biais (remplie de "1") tout a droite
    
    matrice_0 = np.random.randn(m, n).astype(np.float16) # Genère une matrice aléatoire de distribution normale
    matrice_1 = np.ones((m,1)).astype(np.float16) # Génère une matrice biais
    
    # concatenate the two matrices created just before.
    matrice_biais = np.concatenate((matrice_0, matrice_1), axis=1)   
    
    return matrice_biais


Matrice = initialisation(3,3)
print(Matrice)


#correction

def initialisation_1(m,n):
    
    X = np.random.randn(m,n)
    X = np.concatenate((X, np.ones((X.shape[0], 1))), axis=1)

    return X

Y = initialisation_1(3,3)
print(Y)

