# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:42:43 2018

@author: giuschil
"""

#esempi di ricorsione 

#hanoi

def hanoi(quanti_dischi,piolo1,piolo2,piolo3):
    if quanti_dischi == 1:
        print(f"{piolo1}-{piolo2}")
    else:
        hanoi(quanti_dischi-1,piolo1,piolo3,piolo2) #sposto i a e b al piolo3
        print(f"{piolo1}-{piolo2}")
        hanoi(quanti_dischi-1,piolo3,piolo2,piolo1) 
    
def fattoriale(n):
    if n == 1:
        return 1 
    else: 
        return n*fattoriale(n-1)
    
 
def fibo(n):
    if n == 1 or n == 2:
        return 1 
    else: 
        return fibo(n-1)+fibo(n-2)
    

def stampa_fibo(l):
    """Stampa sequenza di fibonacci da una lista di numeri"""
    lista = []
    for i in range(0,len(l)):
        lista.append(fibo(l[i]))
    print(lista)
    
#inverti stringa con ricorsione
    
def inverti(stringa):
    if len(stringa)==1:
        return stringa 
    else:
        return stringa[len(stringa)-1] + inverti(stringa[:-1])

stringa = "mondo ma che cazzo dici "

for i in range(1,2): 
    print(stringa[::-i],end ="")
    
def inverti2(stringa):
    for i in range(1,2): 
        return stringa[::-i] 
    
def conto_alla_rovescia(t):
    print(t)
    if t == 0 :
        return  0
    else:
        return conto_alla_rovescia(t-1)
    
    
for i in range(10,1,-1):
    print(i)

