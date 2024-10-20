'''
Radix Sort è un algoritmo di ordinamento non comparativo che ordina gli elementi basandosi su ogni cifra individuale, partendo dalla cifra meno significativa fino a quella più significativa (o viceversa).
La complessità temporale del Radix Sort è O(kn), dove k è il numero di cifre nel numero massimo.
'''


def radix_sort(arr):
    """
    Implementazione del Radix Sort in Python.
    """
    # Trova il numero massimo nell'array per determinare il numero di cifre
    max_num = max(arr)

    # Ordina partendo dalla cifra meno significativa
    exp = 1
    while max_num / exp > 0:
        counting_sort(arr, exp)
        exp *= 10
def counting_sort(arr, exp1):
    """
    Funzione di supporto per il Radix Sort.
    Implementa l'Ordine per Conteggio basato sulla cifra corrente.
    """
    
    n = len(arr)
    # L'output sarà l'array ordinato
    output = [0] * n
    # Inizializza un array di conteggio come 0
    count = [0] * 10