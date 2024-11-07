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
