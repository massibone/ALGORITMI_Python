'''
Il Meta Binary Search è un'algoritmo che combina 
l'approccio della ricerca binaria con un ulteriore livello 
di ricerca per ottimizzare ulteriormente la ricerca in un elenco ordinato. 
Questo tipo di approccio può essere particolarmente utile in situazioni 
in cui la dimensione dell'elenco non è nota a priori o può variare dinamicamente.
'''

def meta_binary_search(arr, target):
    n = len(arr)
    k = 4  # Numero di intervalli iniziali per la ricerca "meta"
    
    # Fase di ricerca "meta"
    low = 0
    high = n - 1
    interval_size = (high - low + 1) // k
    
    while low <= high:
        found = False
        for i in range(k):
            start = low + i * interval_size
            end = min(start + interval_size - 1, high)
            
            if arr[start] <= target <= arr[end]:
                low = start
                high = end
                found = True
                break
        
        if not found:
            return -1  # Elemento non trovato nel range attuale
    
    # Fase di ricerca binaria standard all'interno del range ottimale trovato
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Elemento non trovato

# Esempio di utilizzo
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
target = 16

result = meta_binary_search(arr, target)
if result != -1:
    print(f"L'elemento {target} è presente nella posizione {result}.")
else:
    print(f"L'elemento {target} non è presente nell'array.")
