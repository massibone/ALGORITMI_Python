def insertion_sort(arr, left=0, right=None):
    """
    Implementa l'ordinamento per inserimento su una porzione dell'array.
    Args:
        arr: Array da ordinare
        left: Indice sinistro della porzione da ordinare
        right: Indice destro della porzione da ordinare
    """
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, left, mid, right):
    """
    Unisce due porzioni ordinate dell'array in-place.
    Args:
        arr: Array contenente le porzioni da unire
        left: Indice di inizio della prima porzione
        mid: Indice di fine della prima porzione
        right: Indice di fine della seconda porzione
    """
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def timsort(arr):
    """
    Implementa l'algoritmo Timsort.
    Args:
        arr: Array da ordinare
    Returns:
        Array ordinato
    """
    if not arr:
        return arr

    n = len(arr)
    if n < 2:
        return arr

    min_run = 32

    # Fase 1: Ordina runs usando insertion sort
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), (n - 1)))

    # Fase 2: Unisci runs
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2

    return arr

def test_timsort():
    """
    Funzione di test per verificare l'implementazione del Timsort.
    """
    test_cases = [
        [],
        [1],
        [2, 1],
        [4, 3, 2, 1],
        [1, 2, 3, 4],
        list(range(100, 0, -1)),
        [3] * 10,
        [1, 2, 3, 3, 3, 4, 5]
    ]
    
    for arr in test_cases:
        original = arr.copy()
        sorted_arr = timsort(arr.copy())
        print(f"Input: {original}")
        print(f"Output: {sorted_arr}")
        print(f"Correctly sorted: {sorted_arr == sorted(original)}\n")