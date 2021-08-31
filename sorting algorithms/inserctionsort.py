# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:23:07 2019

@author: giuse
"""



#inserction sort 

def random_array():
    import random
    n= int(input("How many numbers you want to generate? "))
    m= int(input("Number Max for choice? "))
    my_random=[]
    for i in range(n):
        my_random.append(random.randrange(1, m, 1))
    return my_random

def check_array(array):
    for a in range(0,len(array)-1):
        if array[a] <= array[a+1]:
            continue
        else:
            return False
    return True


array = [4,5,3,7,8,9,1]


for i in range(0,len(array)):
    for j in range(i,len(array)):
        if array[j] < array[i]:
            while j!=0:
                tmp=array[i]
                array[i]= array[j]
                array[j] = tmp
                j-=1
            continue
print(array)


array = random_array()


while check_array(array) !=True:
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            if array[j] < array[i]:
                while j!=0:
                    tmp=array[i]
                    array[i]= array[j]
                    array[j] = tmp
                    j-=1
                continue
print(array)

     