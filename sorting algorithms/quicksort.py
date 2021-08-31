# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:10:10 2019

@author: giuse
"""
def check_array(array):
    for i in range(0,len(array)-1):
        if array[i] <= array[i+1]:
            continue
        else:
            return False
    return True


array_nonordinato = [10,20,5,67,32,45,67,54,11,15,90,80,54,67,73]

array = array_nonordinato

x = len(array)-1 #ultimo elemento dell'array
pivot = array[x] #primo pivot


for i in range(0,x):
    for j in range(i+1,x):
        if array[i] > array[j]:
            tmp = array[i]
            array[j] = array[i]
            array[i] = tmp 


if j< pivot:
    for i in range(0,x):
        for j in range(i+1,x):
            if array[i] > array[j]:
                tmp = array[i]
                array[j] = array[i]
                array[i] = tmp 
            continue 

  
pivot =array[0]  
i=pivot-1

for j in range(len(array),j<=pivot,-1):
    for i in range(0,i>=pivot):
        if i<j:
            tmp= array[i] 
            array[j]=array[i]
            array[i]=tmp
        continue 


def partition(array,p,r):
    pivot =array[p]  
    i=p-1
    for j in range(p,r):
        if array[j] <=pivot:    
            i = i+1
            arr[i],arr[j] =arr[j],arr[i]
         arr[i+1],arr[high] =arr[high],arr[i+1]
        

def quicksort(array,p,r):
    if p<r: 
        q = partition(array,p,r)
        quicksort(array,p,q)
        quicksort(array,q+1,r)
    return array

    
        
