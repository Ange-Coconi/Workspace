# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:44:38 2024

@author: angec
"""


with open('fichier_1','w') as f:
    for i in range(10):
        f.write(f"{i}^2 = {i**2} \n")
        

import csv
import random



def capitale_aleatoire_depuis_csv(fichier_csv):
    capitales = []
    
    # Lecture du fichier CSV
    with open(fichier_csv, mode='r', encoding='ISO-8859-1') as fichier:
        lecteur_csv = csv.DictReader(fichier, delimiter=';')
 
        # Ajouter chaque capitale à la liste
        for ligne in lecteur_csv:
            capitales.append(ligne["Capitale"])  # On utilise la colonne 'Capitale' du fichier CSV
    
    # Choisir une capitale aléatoirement
    random.seed(5)
    capitale = random.choice(capitales)
    
    return capitale

# Exemple d'utilisation
fichier_csv = 'Pays_Capitales.csv'  # Le fichier doit exister dans le même dossier
print(capitale_aleatoire_depuis_csv(fichier_csv))

        