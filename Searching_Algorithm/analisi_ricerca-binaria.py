'''
Funzione Python che implementi la ricerca binaria per trovare un elemento in una lista ordinata.
'''
def ricerca_binaria(lista, elemento):
    """Implementa la ricerca binaria in una lista ordinata."""
    inizio = 0
    fine = len(lista) - 1
    while inizio <= fine:
        mezzo = (inizio + fine) // 2
        if lista[mezzo] == elemento:
            return mezzo
        elif lista[mezzo] < elemento:
            inizio = mezzo + 1
        else:
            fine = mezzo - 1
    return -1

def main():
    """Programma principale."""
    lista_ordinata = [2, 4, 6, 8, 10]
    elemento = int(input("Inserisci l'elemento da cercare: "))
    indice = ricerca_binaria(lista_ordinata, elemento)
    if indice != -1:
        print(f"L'elemento {elemento} è stato trovato all'indice {indice}")
    else:
        print("L'elemento non è stato trovato")

if __name__ == "__main__":
    main()

