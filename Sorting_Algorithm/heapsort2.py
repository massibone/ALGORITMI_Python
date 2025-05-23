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
  # Costruzione del max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Estrazione degli elementi uno alla volta
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Scambio
        heapify(arr, i, 0)
        
  def get_user_input():
    """
    Ottiene l'input dell'utente per l'array da ordinare.
    
    :return: Una lista di numeri inseriti dall'utente
    """
    try:
        return [int(x) for x in input("Inserisci i numeri separati da spazi: ").split()]
    except ValueError:
        print("Input non valido. Assicurati di inserire solo numeri interi.")
        return get_user_input()
    if __name__ == "__main__":
    # Test con array predefinito
    arr_test = [12, 11, 13, 5, 6, 7]
    print("Test con array predefinito:")
    print("Array originale:", arr_test)
    heap_sort(arr_test)
    print("Array ordinato:", arr_test)
    
     # Test con input dell'utente
    print("\nTest con input dell'utente:")
    user_arr = get_user_input()
    print("Array originale:", user_arr)
    heap_sort(user_arr)
    print("Array ordinato:", user_arr)
    
      # Test con casi limite
    print("\nTest con array vuoto:")
    empty_arr = []
    heap_sort(empty_arr)
    print("Array ordinato (vuoto):", empty_arr)

        print("\nTest con array di un solo elemento:")
    single_element_arr = [42]
    heap_sort(single_element_arr)
    print("Array ordinato (un elemento):", single_element_arr)
    
