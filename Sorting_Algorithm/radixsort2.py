def radix_sort(arr):
    """Implementazione del Radix Sort in Python."""
    if len(arr) <= 1:
        return arr

        max_num = max(arr)
    place_value = 1
    while max_num // place_value > 0:
        counting_sort(arr, place_value)
        place_value *= 10

def counting_sort(arr, place_value):
    """Funzione di supporto per il Radix Sort. Implementa l'Ordine per Conteggio basato sulla cifra corrente."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // place_value) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
