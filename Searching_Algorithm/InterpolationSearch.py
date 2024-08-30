def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= x <= arr[high]:
        # Calcola la stima della posizione dell'elemento
        pos = low + ((high - low) // (arr[high] - arr[low])) * (x - arr[low])
   # Se l'elemento è stato trovato, restituisce il suo indice
        if arr[pos] == x:
            return pos
