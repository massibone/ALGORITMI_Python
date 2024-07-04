def sentinel_linear_search(text, sentinels):
    # Aggiungi parole sentinella alla fine del testo
    text += " " + " ".join(sentinels)
    i = 0
    while text[i:i + max(len(s) for s in sentinels)] not in sentinels:
        i += 1
    # Se la parola sentinella è stata trovata, restituisci l'indice
    for sentinel in sentinels:
        if text[i:i + len(sentinel)] == sentinel:
            return i
    # Se la parola sentinella non è stata trovata, restituisci -1
    return -1

# Lettura del contenuto del file
with open("sentinel_text.txt", "r", encoding="utf-8") as file:
    testo = file.read()

# Parole sentinella
parole_sentinella = ["scienza", "statistica"]

# Ricerca della parola sentinella nel testo
indice = sentinel_linear_search(testo, parole_sentinella)
if indice != -1:
    print(f"Una delle parole sentinella è stata trovata all'indice {indice}.")
else:
    print("Nessuna delle parole sentinella è stata trovata nel testo.")

def find_sentinel_word(text, sentinels, index):
    for sentinel in sentinels:
        if text[index:index + len(sentinel)] == sentinel:
            return sentinel
    return None

parola_trovata = find_sentinel_word(testo, parole_sentinella, 3326)


# Stampare il risultato
if parola_trovata:
    print(f"La parola sentinella trovata all'indice 3326 è: {parola_trovata}")
else:
    print("Nessuna delle parole sentinella è stata trovata all'indice 3326.")