'''
L'algoritmo di ricerca esponenziale è un metodo di ricerca per trovare un elemento in un array ordinato. 
Funziona dividendo ripetutamente l'intervallo di ricerca a metà e controllando se l'elemento si trova nella metà inferiore o superiore.
'''
def ricerca_esponenziale(array, elemento, basso, alto):
'''
  Funzione per implementare la ricerca esponenziale in un array ordinato.
Argomenti:
    array: l'array ordinato in cui cercare
    elemento: l'elemento da cercare
    basso: indice di inizio dell'intervallo di ricerca
    alto: indice di fine dell'intervallo di ricerca

  Restituisce:
    La posizione dell'elemento nell'array se trovato, altrimenti -1.
  '''
  
  # Caso base: l'intervallo di ricerca è vuoto
  if basso > alto:
    return -1

  # Calcola l'indice medio esponenzialmente
  if alto == basso:
    return basso

  mezzo = (basso + alto) // 2

  # Controlla se l'elemento si trova nella metà inferiore
  if array[mezzo] > elemento:
    return ricerca_esponenziale(array, elemento, basso, mezzo - 1)

  # Controlla se l'elemento è l'elemento centrale
  elif array[mezzo] == elemento:
    return mezzo

  # Controlla se l'elemento si trova nella metà superiore
  else:
    return ricerca_esponenziale(array, elemento, mezzo + 1, alto)

# Esempio di utilizzo
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento = 23

risultato = ricerca_esponenziale(array, elemento, 0, len(array) - 1)

if risultato != -1:
  print(f"L'elemento {elemento} è stato trovato in posizione {risultato}")
else:
  print(f"L'elemento {elemento} non è stato trovato nell'array")
