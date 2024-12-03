# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:29:29 2024

@author: angec
"""


classeur = {
    "positif" : [],
    "negatif" : [],
    }

def trier(classeur, nombre):
    #classeur : dictionnaire taille 2
    #nombre
    #Range nombre dans "positif" ou "negatif" de classeur selon le signe de nombre
    if nombre > 0:
        classeur['positif'].append(nombre)
    elif nombre == 0:
        print('ce nombre n\'est positif ni négatif')
    else:
        classeur['negatif'].append(nombre)
    return classeur


Liste = ['chien','chat','lapin','dinosaure']

dict_1 = {k:k**2 for k in range(20)}

dict_2 = {z:y for z, y in enumerate(Liste)}


import temp
a = -12
print(temp.signe(a))