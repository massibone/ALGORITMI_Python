def radix_sort(arr):
    """Implementazione del Radix Sort in Python."""
    if len(arr) <= 1:
        return arr

        max_num = max(arr)
    place_value = 1
    while max_num // place_value > 0:
        counting_sort(arr, place_value)
        place_value *= 10

