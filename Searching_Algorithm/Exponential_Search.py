'''
L'algoritmo di ricerca esponenziale è un metodo di ricerca per trovare un elemento in un array ordinato. 
La ricerca esponenziale inizia con piccoli passi e aumenta esponenzialmente il range di ricerca 
fino a trovare il blocco che potrebbe contenere l'elemento.
Funziona dividendo ripetutamente l'intervallo di ricerca a metà e controllando se l'elemento si trova nella metà inferiore o superiore.
'''


def ricerca_esponenziale(array, elemento):
    """
    Implementazione della ricerca esponenziale per trovare un elemento in un array ordinato.
    Argomenti:
        array: L'array ordinato in cui cercare
        elemento: L'elemento da cercare
    Restituisce:
        La posizione dell'elemento nell'array se trovato, altrimenti -1.
    """
    if array[0] == elemento:
        return 0

    # Trova l'intervallo esponenziale dove potrebbe trovarsi l'elemento
    indice = 1
    while indice < len(array) and array[indice] <= elemento:
        indice *= 2

    # Effettua una ricerca binaria tra basso e min(indice, len(array) - 1)
    return ricerca_binaria(array, elemento, indice // 2, min(indice, len(array) - 1))

# Esempio di utilizzo
array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento = 23

risultato = ricerca_esponenziale(array, elemento)

if risultato != -1:
    print(f"L'elemento {elemento} è stato trovato in posizione {risultato}")
else:
    print(f"L'elemento {elemento} non è stato trovato nell'array")
