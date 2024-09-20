'''
Funziona confrontando coppie di elementi adiacenti e scambiandoli se sono nell'ordine sbagliato. Questo processo si ripete fino a quando l'intero array non è ordinato. Anche se semplice, Bubble Sort è tra i più lenti.
'''

def bubble_sort(arr):
    n = len(arr)

    # Esegui il ciclo esterno n-1 volte
    for i in range(n):
        # Esegui il ciclo interno n-i-1 volte
        for j in range(0, n-i-1):
            # Confronta elementi adiacenti e scambiali se sono nell'ordine sbagliato
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Esempio di utilizzo
arr = [64, 34, 25, 12, 22, 11, 90]

print("Array originale:", arr)
bubble_sort(arr)
print("Array ordinato:", arr)

