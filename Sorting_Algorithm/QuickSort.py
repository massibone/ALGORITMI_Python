'''
Quick Sort è un algoritmo di ordinamento molto efficiente che segue il paradigma "divide et impera". 
L'algoritmo sceglie un elemento come "pivot" e divide l'array in due parti: 
gli elementi minori del pivot e quelli maggiori. Ordina poi ricorsivamente le due parti.
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
