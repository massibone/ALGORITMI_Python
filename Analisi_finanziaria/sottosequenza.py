def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None  # Non ci sono abbastanza elementi per una sottosequenza di lunghezza k

    # Calcola la somma della prima finestra di lunghezza k
    max_sum = sum(arr[:k])
    current_sum = max_sum

    # Scorri la finestra sull'array
    for i in range(k, n):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Esempio di utilizzo
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print("La somma massima di una sottosequenza di lunghezza", k, "è", max_sum_subarray(arr, k))
