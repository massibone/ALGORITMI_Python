def bubble_sort(arr, reverse=False):
    """
    Ordina un array utilizzando l'algoritmo Bubble Sort.

    Args:
        arr (list): L'array da ordinare.
        reverse (bool, optional): Se True, ordina in modo decrescente. Predefinito è False.

    Returns:
        list: L'array ordinato.
    """
    n = len(arr)
    swapped = True

    # Esegui il ciclo finché ci sono scambi
    while swapped:
        swapped = False
        # Esegui il ciclo interno n-1 volte
        for i in range(n-1):
            # Confronta elementi adiacenti e scambiali se sono nell'ordine sbagliato
            if (reverse and arr[i] < arr[i+1]) or (not reverse and arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr
