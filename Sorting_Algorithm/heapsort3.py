'''
heap sort ha il vantaggio di essere un algoritmo in-place (non richiede spazio aggiuntivo) 
rispetto al Merge Sort, che richiede spazio aggiuntivo per le operazioni di fusione.
'''
if __name__ == "__main__":
    # Test con un array misto
    arr = [12, 11, 13, 5, 6, 7]
    print("Array originale:", arr)
    sorted_arr = heap_sort(arr)
    print("Array ordinato:", sorted_arr)
    
