'''
se hai una lista ordinata e vuoi trovare un elemento in modo efficiente, 
la ricerca binaria è la scelta migliore con un tempo di esecuzione.
Tuttavia, se hai una lista non ordinata e desideri migliorare leggermente le prestazioni della ricerca lineare, puoi considerare l'utilizzo della ricerca lineare con sentinella, 
che ha un tempo di esecuzione peggiore
'''

def binary_search(arr, target):
    """
    Implementazione dell'algoritmo di ricerca binaria.

    Parameters:
    arr (list): Una lista ordinata di elementi su cui eseguire la ricerca.
    target: L'elemento da cercare nella lista.

    Returns:
    int: L'indice dell'elemento target nella lista se presente, altrimenti -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Trova l'elemento di mezzo

        # Controlla se l'elemento di mezzo è uguale al target
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1  # Se il target è maggiore, cerca nella metà superiore
        else:
            high = mid - 1  # Se il target è minore, cerca nella metà inferiore

    return -1  # Se l'elemento non è presente nella lista

# Esempio di utilizzo della ricerca binaria
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_element = 23

# Esegui la ricerca binaria nella lista ordinata
result_index = binary_search(sorted_list, target_element)

# Stampiamo il risultato della ricerca binaria
if result_index != -1:
    print(f"L'elemento {target_element} è presente nella lista all'indice {result_index}.")
else:
    print(f"L'elemento {target_element} non è presente nella lista.")
