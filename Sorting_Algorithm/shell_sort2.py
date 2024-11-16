def shell_sort_ciura_sequence(array):
    """
    Implementazione di Shell Sort con la sequenza di gap migliorata di Ciura.
    
    :param array: Lista di elementi da ordinare.
    :return: Lista ordinata.
    """
    # Sequenza di gap di Ciura (migliorata): [701, 301, 132, 57, 23, 10, 4, 1]
    ciura_gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in ciura_gaps:
        if gap < len(array):
            for i in range(gap, len(array)):
                temp = array[i]
                j = i
                
                # Spostamento degli elementi più grandi verso destra
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                
                # Inserimento dell'elemento nella posizione corretta
                array[j] = temp
    
    return array
