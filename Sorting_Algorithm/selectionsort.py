'''
Il Selection Sort divide l'input in una parte ordinata e una parte non ordinata. Ad ogni iterazione, trova l'elemento minimo nella parte non ordinata e lo sposta nella parte ordinata.

Entrambi questi algoritmi sono semplici da implementare ma non sono efficienti per grandi insiemi di dati. La loro complessità temporale è O(n^2) nel caso medio e nel caso peggiore, dove n è il numero di elementi nell'array.

Per set di dati più grandi, algoritmi più efficienti come QuickSort, MergeSort o HeapSort sarebbero preferibili.
'''
'''
Selection Sort: Questo algoritmo seleziona ripetutamente l'elemento minimo (o massimo) dalla parte non ordinata dell'array e lo sposta alla posizione corretta. È facile da implementare ma inefficiente per grandi quantità di dati, avendo una complessità temporale di O(n^2)
'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
selectiotionsort2.py
def selection_sort(arr):
    n = len(arr)

    # Scorrere tutti gli elementi dell'array
    for i in range(n):
        
        # Trovare il minimo elemento dall'array non ordinato
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
