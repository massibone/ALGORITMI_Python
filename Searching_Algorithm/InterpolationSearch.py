def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high and arr[low] <= x <= arr[high]:
        # Avoid division by zero
        if arr[high] == arr[low]:
            if arr[low] == x:
                return low
            else:
                return -1
        
        # Corrected calculation of the estimated position (pos)
        pos = low + int(((high - low) / (arr[high] - arr[low])) * (x - arr[low]))
        
        # Check if the element is found at pos
        if arr[pos] == x:
            return pos
        
        # If the element is larger, search in the right sub-array
        if arr[pos] < x:
            low = pos + 1
        
        # If the element is smaller, search in the left sub-array
        else:
            high = pos - 1
    
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11
result = interpolation_search(arr, x)
if result != -1:
    print("Elemento", x, "trovato all'indice", result)
else:
    print("Elemento", x, "non trovato nell'array")
