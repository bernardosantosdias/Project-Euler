#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:12:57 2018

@author: bernardo
"""

a = 1
b = 2
lista = []
somatorio = 2

while b < 4E6:
    c = a + b
    a = b
    #print('b', b)
    b = c
    #print(c)
    div = c % 2
    
    if div == 0:
        lista.append(c)
        
for i in lista:
    somatorio = somatorio + i


print(lista)    
print(somatorio)