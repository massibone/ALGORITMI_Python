'''
One-Sided Binary Search, also known as Exponential Search or Galloping Search, is a variation of binary search optimized for unbounded or infinite lists where the size of the list is not known beforehand. This search technique is particularly useful when dealing with large or continuously growing datasets.
'''
'''
One-Sided Binary Search espande dinamicamente l'intervallo di ricerca, 
mentre Meta Binary Search divide l'elenco in intervalli fissi e 
cerca l'intervallo contenente il valore cercato. 
Entrambi i metodi combinano la velocità dell'espansione rapida 
dell'intervallo con la precisione della ricerca binaria per migliorare 
le prestazioni della ricerca su grandi dataset.
'''
def one_sided_binary_search(arr, target):
    n = len(arr)
    
    # Step 1: Find the range [left, right] where the target might be present
    if arr[0] == target:
        return 0  # Target is found at the first element
    
    left = 1
    right = 1
    
    # Exponentially increase the range
    while right < n and arr[right] < target:
        left = right
        right *= 2
    
    # Step 2: Perform binary search within the identified range [left, right]
    return binary_search(arr, target, left, min(right, n - 1))

def binary_search(arr, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
target = 13

index = one_sided_binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
