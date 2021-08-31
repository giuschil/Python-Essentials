###### Chapter 1 excercies Python Book #####
# Excercies 1 
# Exercise 4.1 Define three variables var1, var2 and var3. Calculate the average of these 
# variables and assign it to average. Print the average. Add three comments.



def threeNumberAvg(var1,var2,var3):
    return float((var1+var2+var3)/3)

print("Il programma calcola la media di tre numeri")
print("Inserisci tre numeri per calcolare la media ")
print("Inserisci var1: ")
var1 = int(input())

print("Inserisci var2: ")
var2 = int(input())

print("Inserisci var3: ")
var3 = int(input())

print("var2: ",var2)
print("var3: ",var3)

print("la media è {0:.3f}".format(threeNumberAvg(var1,var2,var3)))
