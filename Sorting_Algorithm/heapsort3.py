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
    
    # Test con un array già ordinato
    arr_ordinato = [1, 2, 3, 4, 5]
    print("Array ordinato originale:", arr_ordinato)
    sorted_arr_ordinato = heap_sort(arr_ordinato)
    print("Array ordinato dopo heap sort:", sorted_arr_ordinato)
    
    # Test con un array inversamente ordinato
    arr_inverso = [5, 4, 3, 2, 1]
    print("Array inverso:", arr_inverso)
    sorted_arr_inverso = heap_sort(arr_inverso)
    print("Array ordinato dopo heap sort:", sorted_arr_inverso)
