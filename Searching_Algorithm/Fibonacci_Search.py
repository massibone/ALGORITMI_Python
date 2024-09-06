'''
Si basa sulla successione di Fibonacci per dividere ripetutamente l'intervallo di ricerca in proporzioni ottimali.
'''
def ricerca_fibonacci(array, elemento, basso, alto):
  """
  Funzione per implementare la ricerca di Fibonacci in un array ordinato.

  Argomenti:
    array: l'array ordinato in cui cercare
    elemento: l'elemento da cercare
    basso: indice di inizio dell'intervallo di ricerca
    alto: indice di fine dell'intervallo di ricerca

  Restituisce:
    La posizione dell'elemento nell'array se trovato, altrimenti -1.
  """

  # Caso base: l'intervallo di ricerca è vuoto
  if basso > alto:
    return -1

  # Calcola il numero di Fibonacci giusto per l'intervallo di ricerca
  fib_meno_due = alto - basso + 1
  i = 0
  while (fib_meno_due > 0):
    fib_meno_due = fib_meno_due // 2
    i += 1

  # Calcola l'offset finale
  offset = fib_meno_due - 1

  # Cerca l'elemento nella parte destra dell'intervallo ridotto
  if array[alto - offset] > elemento:
    return ricerca_fibonacci(array, elemento, basso, alto - offset - 1)

  # Controlla se l'elemento è l'elemento all'offset
  elif array[alto - offset] == elemento:
    return alto - offset

  # Cerca l'elemento nella parte sinistra dell'intervallo ridotto
  else:
    return ricerca_fibonacci(array, elemento, basso + offset, alto)

# Esempio di utilizzo
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento = 23

risultato = ricerca_fibonacci(array, elemento, 0, len(array) - 1)

if risultato != -1:
  print(f"L'elemento {elemento} è stato trovato in posizione {risultato}")
else:
  print(f"L'elemento {elemento} non è stato trovato nell'array")
