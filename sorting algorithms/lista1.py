# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:44:09 2019

@author: giuse
"""

a = []

n= int(input(("quanti numeri nella lista?")))

for x in range(0,n):
    element= int(input(("inserisci i numeri: ")))
    a.append(element)
    
print(a)

tmp= a[0]
a[0]=a[n-1]
a[n-1]=tmp

print(a)


