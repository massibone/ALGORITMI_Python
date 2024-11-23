'''
Bucket Sort divide l'array originale in un certo numero di "secchi" (bucket), 
e poi ordina ogni secchio individualmente usando un altro algoritmo di ordinamento (spesso Insertion Sort o Merge Sort). 
Infine, i secchi ordinati vengono combinati per ottenere l'array finale ordinato.
'''
def bucket_sort(arr, num_buckets):
  '''
  Implementa l'algoritmo di Bucket Sort.

  Args:
    arr: L'array da ordinare.
    num_buckets: Il numero di bucket da utilizzare.

  Returns:
    L'array ordinato.
  '''

  # Trova il valore minimo e massimo nell'array
  min_val = min(arr)
  max_val = max(arr)

  # Calcola la dimensione di ogni bucket
  bucket_size = (max_val - min_val) // num_buckets + 1

  # Crea una lista di bucket vuoti
  buckets = [[] for _ in range(num_buckets)]

  # Distribuisci gli elementi nei bucket
  for num in arr:
    bucket_index = (num - min_val) // bucket_size
    buckets[bucket_index].append(num)

  # Ordina ogni bucket usando Insertion Sort
  for i in range(num_buckets):
    insertion_sort(buckets[i])

  # Concatena i bucket ordinati per ottenere l'array finale ordinato
  result = []
  for bucket in buckets:
    result.extend(bucket)

  return result
def insertion_sort(arr):
  """
  Implementa l'algoritmo di Insertion Sort.

  Args:
    arr: L'array da ordinare.
  """
