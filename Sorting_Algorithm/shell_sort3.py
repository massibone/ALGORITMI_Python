import time

# Sequenza di gap di Ciura: [701, 301, 132, 57, 23, 10, 4, 1]
CIURA_GAPS = [701, 301, 132, 57, 23, 10, 4, 1]
def shell_sort_ciura_sequence(array):
    '''
    Implementazione di Shell Sort con la sequenza di gap migliorata di Ciura.
    :param array: Lista di elementi da ordinare.
    :return: Lista ordinata.
    '''
    if len(array) <= 1:
        return array

    for gap in CIURA_GAPS:
        if gap < len(array):
            for i in range(gap, len(array)):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
    return array

def test_shell_sort(array):
    print("Array originale:", array)
    start_time = time.time()
    sorted_array = shell_sort_ciura_sequence(array.copy())
    end_time = time.time()
    print("Array ordinato:", sorted_array)
    print(f"Tempo di esecuzione: {end_time - start_time:.6f} secondi")
    print("Ordinamento corretto:", sorted_array == sorted(array))
    print()
