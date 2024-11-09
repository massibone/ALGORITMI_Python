'''
Shell Sort è una generalizzazione dell'insertion sort che permette agli elementi di essere scambiati tra loro a distanze maggiori,
riducendo gradualmente queste distanze. Si basa su una sequenza di gap per migliorare l'efficienza rispetto all'Insertion Sort.
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
