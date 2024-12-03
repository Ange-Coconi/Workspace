# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:26:30 2024

@author: angec
"""
from scipy import misc
import matplotlib.pyplot as plt
face = misc.face(gray=True)
plt.imshow(face, cmap=plt.cm.gray) 
plt.show()   


dface = face.shape                      # Dimension de l'image
left_edge = int(dface[0]/2 -  dface[0]/4)     #left edge of the image after a zoom 1/4
right_edge = int(dface[0]/2 + dface[0]/4)    #right edge of the image after a zoom 1/4
top_edge = int(dface[1]/2-  dface[1]/4)      #top edge of the image after a zoom 1/4
bottom_edge = int(dface[1]/2 + dface[1]/4)   #bottom edge of the image after a zoom 1/4

face_un_quart = face[left_edge : right_edge, top_edge : bottom_edge] 

face_un_quart[face_un_quart>200] = 255
face_un_quart[face_un_quart<50] = 0

plt.imshow(face_un_quart, cmap=plt.cm.gray) 
plt.show()

# correction 
h = face.shape[0]
w = face.shape[1]
zoom_face = face[h//4 : -h//4 , w//4 : -w//4]

plt.imshow(zoom_face, cmap=plt.cm.gray)
plt.show