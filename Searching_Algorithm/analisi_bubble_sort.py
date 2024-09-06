'''
Questa versione ottimizzata mantiene la stessa complessità nel caso peggiore, 
ma può terminare prima nel caso migliore, avvicinandosi a O(n) per array quasi ordinati.
'''

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
