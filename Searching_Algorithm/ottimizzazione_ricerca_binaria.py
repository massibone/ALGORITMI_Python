import random
import time

def genera_lista_ordinata(n):
    return sorted([random.randint(1, 1000000) for _ in range(n)])

def ricerca_lineare(lista, elemento):
    for i, valore in enumerate(lista):
        if valore == elemento:
            return i
    return -1
