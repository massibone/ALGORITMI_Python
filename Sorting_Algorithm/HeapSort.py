'''
Heap Sort si basa su una struttura dati chiamata "heap", 
che è un albero binario completo. 
L'algoritmo costruisce un max-heap 
(o min-heap) dall'array e poi estrae 
l'elemento massimo (o minimo), ricostruendo il heap finché l'array non è ordinato.

'''
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Costruzione del max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Estrazione degli elementi uno alla volta
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Scambio
        heapify(arr, i, 0)

    return arr

# Esempio di utilizzo
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Array originale:", arr)
    sorted_arr = heap_sort(arr)
    print("Array ordinato:", sorted_arr)
