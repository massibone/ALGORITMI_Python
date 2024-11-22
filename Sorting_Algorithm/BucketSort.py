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
