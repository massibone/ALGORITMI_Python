import random
import time

def genera_lista_ordinata(n):
    return sorted([random.randint(1, 1000000) for _ in range(n)])

def ricerca_lineare(lista, elemento):
    for i, valore in enumerate(lista):
        if valore == elemento:
            return i
    return -1
def ricerca_binaria(lista, elemento):
    sinistra, destra = 0, len(lista) - 1
    while sinistra <= destra:
        medio = (sinistra + destra) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            sinistra = medio + 1
        else:
            destra = medio - 1
    return -1

# Genera una lista grande e ordinata
n = 1000000
lista_grande_ordinata = genera_lista_ordinata(n)

# Elemento da cercare
elemento_da_cercare = random.choice(lista_grande_ordinata)

# Test ricerca lineare
inizio = time.time()
indice_lineare = ricerca_lineare(lista_grande_ordinata, elemento_da_cercare)
fine = time.time()
tempo_lineare = fine - inizio

# Test ricerca binaria
inizio = time.time()
indice_binario = ricerca_binaria(lista_grande_ordinata, elemento_da_cercare)
fine = time.time()
tempo_binario = fine - inizio

print(f"Tempo ricerca lineare: {tempo_lineare:.6f} secondi")
print(f"Tempo ricerca binaria: {tempo_binario:.6f} secondi")
print(f"Speedup: {tempo_lineare / tempo_binario:.2f}x")
print(f"Indice trovato (lineare): {indice_lineare}")
print(f"Indice trovato (binario): {indice_binario}")
