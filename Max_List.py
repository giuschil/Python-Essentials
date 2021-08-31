# Excercies 2
# Populate a list with 20 numbers of your choice. After insertion, all elements of the list are displayed with their index.
# After finding the maximum value among those included in the list.

array = []
endList = int(input("inserisci la lunghezza della lista: " ))

for i in range(endList):
    num = int(input("Scrivi un numero: "))
    array.append(num)

for i in range(endList):
    print(array[i],end =",")
		

def maxList(array):
    max = array[0]
    lenghList = len(array)
    for i in range(lenghList):
        if max < array[i]:
            max = array[i]
    return max

print(maxList(array))

def minList(array):
    min_array = array
    min = min_array[i]
    lenghList = len(min_array)
    for i in range(lenghList):
        if min > min_array[i]:
            min = min_array[i]
    return min


print(minList(array))

