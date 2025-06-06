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
    
    # Passo 4: Calcolare le posizioni cumulative nell'array di conteggi
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    
    # Passo 5: Costruire l'array ordinato utilizzando le posizioni cumulative
    sorted_array = [0] * len(array)
    for num in array:
        sorted_array[count_array[num - min_value] - 1] = num
        count_array[num - min_value] -= 1
    
    return sorted_array

   #   Esempio di utilizzo
   if __name__ == "__main__":
        array_di_esempio = [4, 2, 2, 8, 3, 3, 1]
        print("Array originale:", array_di_esempio)
        print("Array ordinato con Counting Sort:", counting_sort(array_di_esempio))


