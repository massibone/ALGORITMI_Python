def heapify(arr, n, i):
    """
    Mantiene la proprietà del max-heap per il sottoalbero radicato all'indice i.
    
    :param arr: L'array da heapify
    :param n: La dimensione del heap
    :param i: L'indice radice del sottoalbero
    """
    largest = i
    while True:
        left = 2 * i + 1
        right = 2 * i + 2

