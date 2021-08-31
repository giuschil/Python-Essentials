# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:05:48 2019

@author: giuse
"""

def check_array(array):
    for a in range(0,len(array)-1):
        if array[a] <= array[a+1]:
            continue
        else:
            return False
    return True


array = [34,5,3,7,8,9,1]

while check_array(array) !=True:
    for i in range(0,len(array)):
        tmp = array[i]
        for j in range(i,len(array)):
            if array[j] < tmp:
                while j!=0:
                    tmp=array[i]
                    array[i]= array[j]
                    array[j] = tmp
                    j-=1
                continue   
print(array)

