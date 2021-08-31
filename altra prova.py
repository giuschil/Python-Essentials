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


path="F:\prova"

def cesare_cifra(path):
    fh = open(path+".txt")
    buffer = fh.readlines()
    vec_lines=[]
    for stringa in buffer:
        parola = ""
        for i in range( 0, len(stringa) ): 
            if stringa[i]<"a" or stringa[i]>"z":
                parola += stringa[i]
            else:
                parola +=(chr((ord(stringa[i])+3-ord("a"))%26+ord("a")))
        vec_lines.append(parola) 
    fh.close()
    fh = open(path+"ENC.txt","w")
    for line in vec_lines:
        fh.write(line)
    fh.close()

cesare_cifra(path)


def cesare_cifra(path):
    fh = open(path+".txt")
    fhw = open(path+"ENC.txt","w")
    buffer = fh.readlines()
    for stringa in buffer:
        parola = ""
        for i in range( 0, len(stringa) ): 
            if stringa[i]<"a" or stringa[i]>"z":
                parola += stringa[i]
            else:
                parola +=(chr((ord(stringa[i])+3-ord("a"))%26+ord("a")))
        fhw.write(parola) 
    fh.close()
    fhw.close()
    
cesare_cifra(path)








def cesare_decifra(stringa):
    for i in range( 0, len( stringa ) ): 
        parola =""
        if stringa[i]==" ":
            parola += chr(32)
        else:
            parola +=((chr(ord(stringa[i])-3)))
        print(parola,end="")
cesare_decifra("phhw |rx lq wkh sdun")



fp = open("F:\prova_esame.txt")
"""
while True:
    buffer = fp.readline()
    if buffer == "":
        break
    print(buffer)
"""
buffer = fp.readlines()
for line in buffer:
    print(line)
fp.close()

fp= open("F:\prova_esame.txt")
print(fp.read())
fp.close




fp= open("F:\prova_esame.txt")
stringa=(fp.read())
cesare_cifra(stringa)



