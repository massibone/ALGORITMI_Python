
'''
versione migliorata che riduce iterazioni
'''
def optimized_bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if (reverse and arr[j] < arr[j+1]) or (not reverse and arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
