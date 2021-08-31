# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 22:40:08 2018

@author: giuschil
"""

#programmazione ad oggetti oop 

# voglio creare una classe che crei l'oggetto punto cartesiano 

import math

class Punto: 
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
     
    def to_string(self):
        return f"({str(self.x)},{str(self.y)})"
   
    def __sub__(self,altro_punto):
        cat1 = altro_punto.x -self.x
        cat2 = altro_punto.y -self.y
        ipo_quadrato = math.pow(cat1,2)+math.pow(cat2,2)
        return math.sqrt(ipo_quadrato)
    

  
    
p1 = Punto(18,2)
