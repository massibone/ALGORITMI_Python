'''
Radix Sort è un algoritmo di ordinamento non comparativo che ordina gli elementi basandosi su ogni cifra individuale,
partendo dalla cifra meno significativa fino a quella più significativa (o viceversa).
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
   # Archivia il conteggio di ogni cifra nel conteggio[]
    for i in range(n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Modifica count[i] in modo che count[i] contenga la posizione
    # della cifra corrente nell'output
    for i in range(1, 10):
        count[i] += count[i - 1]

    

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]e
    # Esempio di utilizzo
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)

print("Array ordinato:")
for i in range(len(arr)):
    print(arr[i], end=" ")


