def sentinel_linear_search(text, word):
    # Aggiungi una parola sentinella alla fine del testo
    text += " SENTINEL_WORD"
    i = 0
    while text[i] != "SENTINEL_WORD":
        # Se la parola corrente corrisponde alla parola cercata, restituisci l'indice
        if text[i:i + len(word)] == word:
            return i
        i += 1
    # Se la parola cercata non è stata trovata, restituisci -1
    return -1

# Lettura del contenuto del file
with open("sentinel_text.txt", "r",encoding="utf-8") as file:
    testo = file.read()

# Parola da cercare
parola_da_cercare = "scienza"

# Ricerca della parola nel testo
indice = sentinel_linear_search(testo, parola_da_cercare)
if indice != -1:
    print(f"La parola '{parola_da_cercare}' è stata trovata all'indice {indice}.")
else:
    print(f"La parola '{parola_da_cercare}' non è stata trovata nel testo.")
