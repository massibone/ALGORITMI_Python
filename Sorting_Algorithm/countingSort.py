def counting_sort(array):
    """
    Implementazione dell'algoritmo di Counting Sort per ordinare un array di numeri interi.
    
    :param array: Lista di numeri interi con un range limitato.
    :return: Lista ordinata in senso crescente.
    """
    # Passo 1: Trovare il valore massimo e minimo nell'array per determinare la dimensione dell'array di conteggi
    min_value = min(array)
    max_value = max(array)
    
  # Passo 2: Creare un array di conteggi, con dimensione pari alla differenza tra il valore massimo e minimo più uno
    count_array = [0] * (max_value - min_value + 1)
    

    # Passo 3: Contare le occorrenze di ogni valore nell'array originale
    for num in array:
        count_array[num - min_value] += 1
    
