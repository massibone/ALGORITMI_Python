def heapify(arr, n, i):
    '''
    Mantiene la proprietà del max-heap per il sottoalbero radicato all'indice i.
    
    :param arr: L'array da heapify
    :param n: La dimensione del heap
    :param i: L'indice radice del sottoalbero
    '''
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest == i:
            break
        
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

def heap_sort(arr):
    '''
    Ordina un array utilizzando l'algoritmo Heap Sort.
    
    :param arr: L'array da ordinare
    :return: None (l'array viene ordinato in-place)
    '''
    if not arr:
        return  # Gestione del caso di array vuoto
    
    n = len(arr)
    
