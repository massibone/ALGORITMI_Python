def counting_sort(array):
    """
    Implementazione dell'algoritmo di Counting Sort per ordinare un array di numeri interi.
    
    :param array: Lista di numeri interi con un range limitato.
    :return: Lista ordinata in senso crescente.
    """
    # Passo 1: Trovare il valore massimo e minimo nell'array per determinare la dimensione dell'array di conteggi
    min_value = min(array)
    max_value = max(array)
    
