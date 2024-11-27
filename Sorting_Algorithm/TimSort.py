'''
Tim Sort è un algoritmo ibrido, utilizzato in molte librerie standard (come Python). 
Combina le tecniche di Merge Sort e Insertion Sort per ottimizzare le prestazioni su dataset reali, 
in particolare quelli che hanno già porzioni di dati ordinati.
'''

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1

        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key_item
