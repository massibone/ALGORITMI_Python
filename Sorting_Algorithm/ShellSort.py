'''
Shell Sort è una generalizzazione 
dell'insertion sort che permette 
agli elementi di essere scambiati 
tra loro a distanze maggiori,
riducendo gradualmente queste distanze. 
Si basa su una sequenza di gap per 
migliorare l'efficienza rispetto 
all'Insertion Sort.
'''

def shell_sort_shell_sequence(array):
    """
    Implementazione di Shell Sort con la sequenza di gap originale di Shell.
    
    :param array: Lista di elementi da ordinare.
    :return: Lista ordinata.
    """
    # Sequenza di gap di Shell (originale): inizia con metà della lunghezza dell'array e dimezza ad ogni passo
    gap = len(array) // 2
    
    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i

            
            # Spostamento degli elementi più grandi verso destra
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            
   
            
            # Spostamento degli elementi più grandi verso destra
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            
   

         # Inserimento dell'elemento nella posizione corretta
            array[j] = temp
        
        # Riduzione della distanza di gap per il prossimo passo
        gap //= 2
    
    return array


# Esempio di utilizzo
if __name__ == "__main__":
    array_di_esempio = [64, 34, 25, 12, 22, 11, 90]
    print("Array originale:", array_di_esempio)
    print("Array ordinato con Shell Sort (sequenza di Shell):", shell_sort_shell_sequence(array_di_esempio))
