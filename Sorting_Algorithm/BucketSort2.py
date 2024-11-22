def bucket_sort(arr, num_buckets):
    """
    Implementa l'algoritmo di Bucket Sort ottimizzato.
    Args:
        arr: L'array da ordinare
        num_buckets: Il numero di bucket da utilizzare
    Returns:
        L'array ordinato
    Raises:
        ValueError: Se l'input non è valido
    """
    # Validazione input
    if not arr:
        return arr
    if num_buckets <= 0:
        raise ValueError("Il numero di bucket deve essere positivo")

    # Trova il valore minimo e massimo nell'array
    min_val = min(arr)
    max_val = max(arr)
    
    # Gestione caso speciale: tutti i valori sono uguali
    if min_val == max_val:
        return arr.copy()
    
    # Calcola la dimensione di ogni bucket
    bucket_size = (max_val - min_val) / num_buckets
    
    # Crea una lista di bucket vuoti
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribuisci gli elementi nei bucket
    for num in arr:
        # Gestione caso speciale per il valore massimo
        bucket_index = int((num - min_val) / bucket_size)
        if bucket_index == num_buckets:
            bucket_index -= 1
        buckets[bucket_index].append(num)
    
    # Ordina ogni bucket usando Insertion Sort o Timsort per bucket grandi
    result = []
    for bucket in buckets:
        if len(bucket) > 32:  # soglia arbitraria per passare a Timsort
            bucket.sort()
        else:
            insertion_sort(bucket)
        result.extend(bucket)
    
    return result

def insertion_sort(arr):
    """
    Implementa l'algoritmo di Insertion Sort.
    Args:
        arr: L'array da ordinare
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Esempio di utilizzo con gestione errori
def test_bucket_sort():
    test_cases = [
        [29, 72, 9, 5, 86, 33, 94, 24, 57, 17, 85, 25],
        [],
        [1],
        [3, 3, 3, 3],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    for arr in test_cases:
        try:
            print(f"Input: {arr}")
            sorted_arr = bucket_sort(arr, 5)
            print(f"Output: {sorted_arr}\n")
        except ValueError as e:
            print(f"Errore: {e}\n")
