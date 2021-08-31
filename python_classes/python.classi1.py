# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:11:08 2018

@author: giuschil
"""

# Classi e Istanze

""" per raggruppare funzioni e variabili 
raggruppare le proprietà in un modello generico,
classe = sistema per modellare la realtà per gestire oggetti complessi 
istanza = ogni oggetto creato dal modello generico(classe)
"""

class Studente:                                 # creo una classe 
    
    def __init__(self,nome,cognome,corso_di_studi):         
        #metodo costruttore, Self se stesso, aggiungo i parametri che deve avere
        #il mio oggetto
        self.nome = nome
        self.cognome = cognome 
        self.corso_di_studi = corso_di_studi    
        #queste tre sono le variabili di istanza
    def scheda_personale(self):
        return f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di Studi: {self.corso_di_studi}" 
                        #altro tipo di formattazione avanzata 
    
    
studente_uno = Studente("Py","Mike","programmazione")
studente_due = Studente("Marta","Stannis","scienze")

print(studente_uno)
print(studente_due)
        
        
print(studente_uno.scheda_personale())     
        
print(Studente.scheda_personale(studente_uno)) 
#posso richiamare metodo su ogni oggetto 



"""EREDITARIETA' """

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
   
#lego studente e insegnante 
#queste due classi erediteranno i parametri da persona 
class Studente(Persona):
    pass
class Insegnante(Persona):
    pass 
    
studente_uno = Studente("Paul","Red",23,"Casa studente")
insegnante_uno =Insegnante("Mario","Rossi",55,"viale roma")
print(studente_uno.scheda_personale())

print(insegnante_uno.scheda_personale())


print(help(Studente))


"""
variabili di istanza = sono quelli impostati con self. e rappresenta 
una referenza a ciascuna classe

variabili di classe = attributi che sono condivisi da ciascuna istanza 
per esempio il numero di ore di lezione(è condivisa sia da studenti che da prof)
si fa all'interno di class
"""
class Studente:                                 # creo una classe 
    
    ore_settimanali = 36        #var di classe sarà condivisa da tt le istanze
    
    def __init__(self,nome,cognome,corso_di_studi):         
        #metodo costruttore, Self se stesso, aggiungo i parametri che deve avere
        #il mio oggetto
        self.nome = nome
        self.cognome = cognome 
        self.corso_di_studi = corso_di_studi    
        #queste tre sono le variabili di istanza
        
    def scheda_personale(self):
        scheda = f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\
                    \n Corso di Studi: {self.corso_di_studi}\
                    \n Ore Settimanali:{self.ore_settimanali}"
                        
                        #altro tipo di formattazione avanzata 
        return scheda
    
studente_uno = Studente("Py","Mike","programmazione")
studente_due = Studente("Marta","Stannis","scienze")

print(studente_uno.scheda_personale())

#incrementa le ore settimanali di uno dello studente nella scheda
studente_uno.ore_settimanali +=5 

print(Studente.__dict__)
print(studente_uno.__dict__)


#altro esempio di variabili di classe 

#aggiungo numero di studenti 

class Studente:                                 # creo una classe 
    
    ore_settimanali = 36        #var di classe sarà condivisa da tt le istanze
    corpo_studentesco = 0       #var di classe numero di studenti
    
    def __init__(self,nome,cognome,corso_di_studi):         
        #metodo costruttore, Self se stesso, aggiungo i parametri che deve avere
        #il mio oggetto
        self.nome = nome
        self.cognome = cognome 
        self.corso_di_studi = corso_di_studi    
        #queste tre sono le variabili di istanza
        Studente.corpo_studentesco +=1 
        
    def scheda_personale(self):
        scheda = f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\
                    \n Corso di Studi: {self.corso_di_studi}\
                    \n Ore Settimanali:{self.ore_settimanali}"
                        
                        #altro tipo di formattazione avanzata 
        return scheda
    
studente_uno = Studente("Py","Mike","programmazione")
studente_due = Studente("Marta","Stannis","scienze")

print(studente_uno.scheda_personale())
#aumento ore di studente uno 
studente_uno.ore_settimanali +=4

#stampo totale corpo studenti 

print(Studente.corpo_studentesco)
# il totale da 2

 

