# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:36:50 2019

@author: giuse
"""

def swap(a,b): 
    tmp = b
    b = a
    a = tmp
    return a,b
    
def random_array():
    import random
    n= int(input("How many numbers you want to generate? "))
    m= int(input("Number Max for choice? "))
    my_random=[]
    for i in range(n):
        my_random.append(random.randrange(1, m, 1))
    return my_random

def check_array(array):
    for i in range(0,len(array)-1):
        if array[i] <= array[i+1]:
            continue
        else:
            return False
    return True

def bubblesort(array):
    while check_array(array) != True:
        for j in range(0,len(array)-1):
            if array[j]>array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1]=tmp 
    return array

 
from datetime import datetime
tstart = datetime.now()
bubblesort(array)
tend = datetime.now()
print(tend - tstart)


if __name__ == '__main__':
    import sys  # importiamo il modulo sys della libreria standard
    import random #importiamo il modulo random per numeri casuali
        
                
                