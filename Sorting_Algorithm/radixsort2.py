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
 i = n - 1
    while i >= 0:
        num = arr[i]
        index = (num // place_value) % 10
        output[count[index] - 1] = num
        count[index] -= 1
        i -= 1
# Esempio di utilizzo
if __name__ == "__main__":
    import time

    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Array originale:", arr)

    start_time = time.time()
    radix_sort(arr)
    end_time = time.time()

    print("Array ordinato:", arr)
    print(f"Tempo di esecuzione: {end_time - start_time:.6f} secondi")
    
    arr[:] = output
