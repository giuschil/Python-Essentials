# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:47:38 2018

@author: giuschil
"""

import re 

#trova inizio e fine delle parole divise tra le virgole in un testo divis
#METODO FINDINTER
regex = r"([a-zA-Z]+) \d+"
matches = re.finditer(regex,"June 24,August 9,Dec 12")
for match in matches:
    print ("Match at index: %s,%s" %(match.start(),match.end()))

#METODO FINDALL
regex = r"([a-zA-Z]+) \d+"
matches = re.findall(regex,"June 24,August 9,Dec 12")
for match in matches:
    print ("Full match: %s" %(match))

 
#METODO REPLACEDSTRING 
    
#riordina la stringa con prima il giorno e poi il mese
# \2 sta per il gg e \1 sta per il mese 

#replacedstring =re.sub(pattern,replacement_pattern,inpup_str,count,flags=0)

regex = r"([a-zA-Z]+) \d+"
print (re.sub(regex,r"\2 of \1", "June 24,August 9,Dec 12" ))

#trovare estensione di un file

#trovare tutte le email che appartengo a 

#rimuovere gli spazi duplicati e gli spazi all'inizio e alla fine " io  e tu "

# rimuovere tutti i tags da html stringa

  
