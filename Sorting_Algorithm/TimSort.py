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

    return arr

def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])

def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), (n - 1)))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(
                arr[start:midpoint], arr[midpoint:end + 1]
            )

            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr

 
