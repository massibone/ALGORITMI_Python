def linear_search(arr, target):
    """
    Esegue la ricerca lineare per trovare l'indice del target nell'array.
    
    :param arr: L'array in cui cercare.
    :param target: Il valore da cercare.
    :return: L'indice del target se presente, altrimenti -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Restituisce l'indice se il target è stato trovato
    return -1  # Ritorna -1 se il target non è stato trovato


# Esempio di utilizzo
arr = [3, 5, 2, 8, 9, 1]
target = 8
result = linear_search(arr, target)

if result != -1:
    print(f"Il target {target} è stato trovato all'indice {result}.")
else:
    print(f"Il target {target} non è stato trovato nell'array.")
