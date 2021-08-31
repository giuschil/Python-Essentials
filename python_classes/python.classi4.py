# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:01:16 2018

@author: giuschil
"""

#METODI SPECIALI CLASSI chiamati DUNDER, INIZIANO CON __  __ W DOPPIO UNDERSCORE
#METODI PER CREARE OGGETTI 


class Studente:
    ore_settimanali = 36 
    
    def __init__(self,nome,cognome,corso_di_studi):
        self.nome = nome
        self.cognome = cognome 
        self.corso_di_studi = corso_di_studi
        
    def scheda_personale(self):
        scheda = f""" 
        Scheda Studente: 
            Nome: {self.nome}
            Cognome: {self.cognome}
            Corso di Studi :{self.corso_di_studi}
            ore_settimanali: {self.ore_settimanali}"""
        return scheda 
    
    #def __add__(self,other):
    #    return self.nome + " " + other.cognome


    #implementazione di metodi DUNDER 
    def __str__(self):              #rappresentazione leggibile per pubblico
       return f"Lo Studente {self.nome} {self.cognome}"
   
    def __repr__(self):             #rappr non ambigua per ricreare oggetto
        return f" Studente('{self.nome}','{self.cognome}','{self.corso_di_studi}')"
    


studente_uno = Studente("Giuseppe","Schillaci","programmazione")

print(studente_uno.scheda_personale())


studente_due = Studente("Marco","Pacifico","economia")

studente_tre = Studente("John","Snow","Antropologia")

#uso add  concatena nome e cognome
#print(studente_uno,studente_due)

print(studente_uno)


#chiamo esplicitamente il dunder methods
#print(Studente.__str__(studente_uno))
#print(Studente.__repr__(studente_uno))


