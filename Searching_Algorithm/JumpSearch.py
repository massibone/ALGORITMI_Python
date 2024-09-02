'''
L'algoritmo di ricerca Jump Search è un metodo di ricerca utilizzato 
per trovare un elemento in un array ordinato. 
Funziona saltando avanti di un certo passo fisso nell'array e quindi confrontando 
l'elemento target con l'elemento corrente.

prende in input un array ordinato arr e un elemento target x. 
L'algoritmo esegue salti di dimensione radice quadrata della lunghezza dell'array 
finché l'elemento corrente è minore del target. Poi, esegue una ricerca 
lineare all'interno del blocco trovato per trovare l'elemento esatto. 
Se l'elemento è trovato, restituisce il suo indice; altrimenti, restituisce -1.

'''

import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Trova il blocco in cui potrebbe essere presente l'elemento
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Esegue una ricerca lineare nel blocco trovato
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    
    # Se l'elemento è stato trovato, restituisce il suo indice
    if arr[prev] == x:
        return prev
    return -1

# Esempio di utilizzo
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
result = jump_search(arr, x)
if result != -1:
    print("Elemento", x, "trovato all'indice", result)
else:
    print("Elemento", x, "non trovato nell'array")
