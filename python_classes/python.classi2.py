# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 19:23:49 2018

@author: giuschil
"""

#vogliamo gestire sia studenti che professori

class Persona:
    def __init__(self,nome,cognome,età,residenza):
        self.nome = nome
        self.cognome = cognome 
        self.età = età 
        self.residenza = residenza 
        
    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        
        return scheda 
    
    def modifica_scheda(self):
        print("""Modifica Scheda:
            1 - Nome
            2 - Cognome
            3 - Età 
            4 - Residenza """)
            
        scelta = input("Cosa desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome --> ")
        if scelta == "2": 
            self.cognome = input("Nuovo Cognome -->")
        if scelta == "3": 
            self.età = input("Nuova Età -->")
        if scelta == "4":
            self.residenza = input("Nuova Residenza -->")
 

    
#uso una funzione SUPER che prende i parametri da __init__     
class Studente(Persona):
    profilo = "Studente"
    
    def __init__(self,nome,cognome,età,residenza,corso_di_studio):
        super().__init__(nome,cognome,età,residenza)
        self.corso_di_studio = corso_di_studio

    def scheda_personale(self):             #metodo Over Writing
        #format avanzata di python 
        scheda = f"""
        Profilo: {Studente.profilo}
        Corso di Studi: {self.corso_di_studio}
        ***""" 
        return super().scheda_personale() + scheda 
            
            
            
class Insegnante(Persona):
    profilo ="Insegnante"
    
    def __init__(self,nome,cognome,età,residenza, materie = None):
        super().__init__(nome,cognome,età,residenza)
        if materie is None:
            self.materie = []
        else: 
            self.materie = materie 

    def scheda_personale(self):
        scheda = f"""
        Profilo: {Insegnante.profilo}
        Materie Insegnate: {self.materie}
        ***""" 
        return super().scheda_personale() + scheda 
    
            
insegnante_uno = Insegnante("Mario","Pedreschi",33,"via San Zeno",["Data Mining1",
                                                                   "Social Network"])
insegnante_due = Insegnante("Giuseppe","Rossi",45,"via Marianna")

studente_uno = Studente("Giuseppe","Schillaci",27,"via San Zeno",["Data Mining1"])


#modifica le scheda con la schermata che abbiamo creato prima 

insegnante_uno.modifica_scheda()
# clicclo su 4 e cambio la residenza per esempio

studente_uno.modifica_scheda()