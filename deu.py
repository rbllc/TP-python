# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

f= lambda x: (3*x+1)/(2*x+1)


def iteration(a,fonction,n):
	liste=[a]
	for k in range(n):
		liste.append(fonction(liste[-1]))
	return liste

from math import sqrt
import numpy as np

def premier(nombre):
    if nombre in [0,1]:
        return False
    if nombre%2==0:
        return False
    for k in range (3,int(sqrt(nombre))+1,2):
        if nombre%k==0:
            return False
    return True

def listePremier(nombre2):
    liste=[2]
    for j in range (nombre2):
        if premier(j)==True:
            liste.append(j)
    return liste

def listePremier2(nombre3):
    liste2=[2]
    test=0
    a=3
    while a<nombre3:
        for j in liste2:
            if a%j!=0:
                test=test+1
        if test==len(liste2):
            liste2.append(a)
        a=a+1
        test=0
    return liste2

import math

def racine(listee):
    newliste=[]
    for a in listee:
        newliste.append(math.sqrt(a))
    return newliste

def mhilb(n):
    liste=[]
    for j in range(n):
        liste.append([1/(i+1+j) for i in range(n)])
    return np.array(liste)

import matplotlib.pyplot as plt 

def dessin():
    x=np.linspace(0,1,1001)
    for i in range (1,10):
        plt.plot(x,x**(i/2),label=f'x**({i}/2)')
    plt.title('dessin')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
