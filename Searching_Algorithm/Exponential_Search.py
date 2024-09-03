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
  
