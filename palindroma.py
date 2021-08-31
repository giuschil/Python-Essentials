#palindroma


#ingegni

def pal(str):
    if str == str[::-1]:
        return True
    return False

# ciao 0,1,2,3
oldString = "provadinuovo"
newString = []

i = len(oldString)

while i > 0: 
    newString.append(oldString[i-1])
    i = i-1

newString = "".join(newString)
print(type(newString))
print(newString)