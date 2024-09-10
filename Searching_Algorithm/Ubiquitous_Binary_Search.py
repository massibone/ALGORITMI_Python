'''
E' simile standard binary search
'''
def binary_search(array, elemento):
  """
  Funzione per implementare la ricerca binaria in un array ordinato.

  Argomenti:
    array: l'array ordinato in cui cercare
    elemento: l'elemento da cercare

  Restituisce:
    La posizione dell'elemento nell'array se trovato, altrimenti -1.
  """


  basso = 0
  alto = len(array) - 1
  mezzo = 0

  while basso <= alto:
    # Calcola l'indice medio
    mezzo = (basso + alto) // 2

    # Controlla se l'elemento è stato trovato
    if array[mezzo] == elemento:
      return mezzo

    # Controlla se l'elemento si trova nella metà inferiore
    elif array[mezzo] > elemento:
      alto = mezzo - 1

    # Controlla se l'elemento si trova nella metà superiore
    else:
      basso = mezzo + 1

  # Elemento non trovato
  return -1

# Esempio di utilizzo
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento = 23

risultato = binary_search(array, elemento)

if risultato != -1:
  print(f"L'elemento {elemento} è stato trovato in posizione {risultato}")
else:
  print(f"L'elemento {elemento} non è stato trovato nell'array")
