"Scrivi funzione che prenda come argomento un numero e restituisca la sequenza di fibonacci fino a quel numero  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,"

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1)+fib(n-2)

