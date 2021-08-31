def polidrome(s):
    indice = (len(s) -1)
    nuova_parola = ""
    while indice >= 0:
        nuova_parola += s[indice]
        indice -= 1
    if nuova_parola == s:
        print(nuova_parola, 'True is a polidrome ')
    else:
        print('False this is not a polidrome')
        
polidrome("anna")



def cesare(stringa):
    for i in range( 0, len( stringa ) ): 
        parola =""
        if stringa[i]==" ":
            parola +=" "
        else:
            parola +=((chr(ord(stringa[i])+3)))
            print(parola,end="")

cesare("meet you in the park")



stringa="meet you in the park"
for i in range(0,len(stringa)): 
    parola =""
    if stringa[i]==" ":
       parola +=(" ")
    else:
       parola +=((chr(ord(stringa[i])+3)))
    print(parola, end="")


 

stringa="phhw |rx lq wkh sdun"
for i in range(0,len(stringa)): 
    parola =""
    if stringa[i]==" ":
       parola +=(" ")
    else:
       parola +=((chr(ord(stringa[i])-3)))
    print(parola, end="")


def cesare_cifra(stringa):
    for i in range(0,len(stringa)): 
        parola =""
        if stringa[i]==" ":
            parola +=" "
        else:
            parola += ((chr(ord(stringa[i])+3)))
            print(parola, end="")

cesare_cifra("ciao mi chiamo")    
    