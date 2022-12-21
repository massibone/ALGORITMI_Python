import datetime
scelta = -1
array_numbers = [64, 26, 93, 27, 97, 31, 44, 55, 20, 41]


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):       # effettua n-1 iterazioni a partire dal secondo elemento della lista
        # salviamo il valore da inserire nella variabile "valore"
        valore = lista[i]
        j = i-1
        # fin quando la condizione del while è verificata,
        while j >= 0 and valore < lista[j]:
            # viene effettuato almeno un spostamento verso destra dei valori maggiori di "valore"
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = valore
    return lista


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def bubbleSort(array):
    len_array = len(array)
    for j in range(0, len_array-1):
        flag = False
        for i in range(0, len_array-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True
        len_array = len_array - 1
        if not (flag):
            break


while (scelta != 0):
    print("-------------------------")
    print("0. Per Uscita")
    print()
    print("1. Ordinamento   base")
    print("2. Ordinamento   Bubble Sort")
    print("3. Ordinamento   Insertion Sort")
    # print("...")
    # print("...")
    print()
    scelta = int(input("Scegli: "))
    print("------------------------")
    if (scelta == 0):
        print("Ciao")
        break
    elif (scelta == 1):
        start_time = datetime.datetime.now()
        print("Operazione --Selection Sort--")
        print(quicksort(array_numbers))
        end_time = datetime.datetime.now()
        print(end_time - start_time)

    elif (scelta == 2):
        start_time = datetime.datetime.now()
        print("Operazione --Bubble Sort--")
        bubbleSort(array_numbers)
        print(array_numbers)
        end_time = datetime.datetime.now()
        print(end_time - start_time)
    elif (scelta == 3):
        print("Operazione --Insertion Sort--")
        print(insertion_sort(array_numbers))

    else:
        print("Non capisco...")
