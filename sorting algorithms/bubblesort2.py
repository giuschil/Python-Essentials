# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:36:50 2019

@author: giuse
"""
import random 

def swap(a,b): 
    tmp = b
    b = a
    a = tmp
    return a,b
    

def random_array():
    my_random=[]
    for i in range(1000):
        my_random.append(random.randrange(1, 100000, 1))
    return my_random


def check_array(array):
    for i in range(0,len(array)-1):
        if array[i] <= array[i+1]:
            continue
        else:
            return False
    return True
        
array = random_array()
array

i=0
while check_array(array) != True:
    for j in range(0,len(array)-1):
        if array[j]>array[j+1]:
            tmp = array[j]
            array[j] = array[j+1]
            array[j+1]=tmp 
 
