# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 21:29:23 2018

@author: giuschil
"""
#aggiungo costruttore_alternativo
# *args per passare parametri che non ci sono nelle sottoclassi
class Persona:
    def __init__(self,nome,cognome,età,residenza):
        self.nome = nome
        self.cognome = cognome 
        self.età = età 
        self.residenza = residenza
	
    @classmethod 	
    def from_string(cls,stringa_persona,*args):		#passo la classe con cls
        nome,cognome,età,residenza = stringa_persona.split("-")
        return cls(nome,cognome,età,residenza,*args)
    
    @classmethod
    def occupazione(cls):
        if cls.__name__ == "Studente":
            return "Studente"
        else: 
            return "Insegnante" 
    
    @staticmethod 
    def info_prog():
        info ="""
        Nome: Persona
        Creato da: Giuschil
        Sito Ufficiale : www.giuschil.com
        Commenti: Scritto con python 3.6
        """
        return info 
    
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
    
#stringa che passo a from_string per prelevare i dati della persona
iron_man = "Tony-Stark-40-Torre Stark"
zuck ="Mark-Zuck-30-California"
persona1 = Persona.from_string(iron_man)

print(persona1.scheda_personale())

insg1 = Insegnante.from_string(iron_man,"Ingegneria")
stud1 = Studente.from_string(zuck,"SEO")

print(insg1.scheda_personale())
print(stud1.scheda_personale())


#provo la static class che ho creato info

print(Persona.info_prog())

