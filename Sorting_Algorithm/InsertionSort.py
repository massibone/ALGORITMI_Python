'''
Inserisce ogni elemento in una sottolista 
ordinata, spostando gli elementi più grandi 
di uno spazio in avanti per fare posto 
al nuovo elemento. 
È più efficiente di Bubble Sort e Selection Sort 
per piccoli set di dati o liste 
già quasi ordinate nel caso peggiore.
'''
def insertion_sort(arr):
    # Inizia dal secondo elemento (indice 1)
    for i in range(1, len(arr)):
        # Elemento da inserire
        key = arr[i]
        
        # Sposta gli elementi di arr[0..i-1] che sono maggiori di key
        # di una posizione avanti rispetto alla loro posizione attuale
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        

        # Inserisce key nella sua posizione corretta
        arr[j + 1] = key

    return arr

# Esempio di utilizzo
if __name__ == "__main__":
    # Lista di esempio
    my_list = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista non ordinata:", my_list)
    
    # Chiamata alla funzione di ordinamento
    sorted_list = insertion_sort(my_list)
    
