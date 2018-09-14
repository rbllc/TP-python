#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 09:34:11 2018

@author: bellec
"""
from math import *

#Exercice 1


def parfait(n):
    somme=0
    for i in range(1,n-1):
        if n%i==0:
            somme=somme+i
    return somme==n

def somdiv(n):
    somme=0
    for i in range(2,int(sqrt(n)) +1):
        if n%i==0:
            if i==n/i:
                somme=somme+i
            else:
                somme=somme+i+n/i
    return int(somme+1)

def amicaux(n,m):
    return somdiv(n)==somdiv(m)

def nbrprft(n):
    liste=[]
    for i in range (1,n):
        if parfait(i)==1:
            liste.append(i)
    return liste

def nbramicx(n):
    liste=[]
    for i in range (1,n):
        a=somdiv(i)
        for j in range (i+1,n):
            if a==j and somdiv(j)==i:
                liste.append([i,j])
    return liste

#Exercice 2



def premier(nombre):
    if nombre in [0,1]:
        return False
    if nombre%2==0:
        return False
    for k in range (3,int(sqrt(nombre))+1,2):
        if nombre%k==0:
            return False
    return True

def chancx(p):
    k=0
    while k<=(p-2):
        if premier(p+k**2+k)==0:
            return 1==0
        k=k+1
    return 1==1

def nbrchancx(n):
    liste=[]
    for i in range (1,n):
        if chancx(i)==1:
            liste.append(i)
    return liste

#Exercice 3
    
def taxicab(n):
    test=0
    fin=int(n**(1/3))+1
    for i in range (1,fin-1):
        a=n-i**3
        for j in range (i,fin):
            if a==j**3:
                test=test+1
    return test

def nbrtaxicab(n):
    liste=[]
    for i in range (1,n):
        if taxicab(i)>1:
            liste.append(i)
    return liste

def taxicabexact(n):
    liste=[]
    for i in range (1,int(n**(1/3))+1):
        b=(n-i**3)**(1/3)
        if b==int(b) and b>i:
            liste.append([i,b])
    return liste

#Exercice 4


def decomp(n):
    liste=[]
    while n!= 0:
        liste.append(n%10)
        n = n//10
    liste.reverse()
    return liste

def decomp2(n):
    n=list(str(n))
    return n

def conway2(x):
    x=decomp2(x)
    long=len(x)
    liste=[]
    test=0
    nombre=[]
    for i in range(1,long):
        if (x[i-1]==x[i]):
            test=test+1
        else:
            liste.append(test+1)
            test=0
            nombre.append(int(x[i-1]))
    liste.append(test+1)
    nombre.append(int(x[i]))
    algo=''
    for j in range(0,len(liste)):
        algo=algo+str(liste[j])+str(nombre[j])
    return int(algo)

def conway(x):
    x=decomp(x)
    long=len(x)
    liste=[]
    test=0
    nombre=[]
    for i in range(1,long):
        if x[i-1]==x[i]:
            test=test+1
        else:
            liste.append(test+1)
            test=0
            nombre.append(x[i-1])
    liste.append(test+1)
    nombre.append(x[i])
    algo=''
    for j in range(0,len(liste)):
        algo=algo+str(liste[j])+str(nombre[j])
    return int(algo)

def nbrconway(N):
    lister=[1]
    new=11
    for ik in range(N):
        lister.append(new)
        new=conway(new)
    return lister

def nbrconway2(N):
    lister=[1]
    new=11
    for ik in range(N):
        lister.append(new)
        new=conway2(new)
    return lister