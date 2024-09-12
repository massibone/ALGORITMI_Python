'''
Data una funzione Python che legge un file di testo e restituisce una lista di parole ordinate per frequenza di apparizione, 
scomponi la funzione in sotto-funzioni che svolgono compiti specifici (es. lettura file, elaborazione testo, ordinamento).
'''
def leggi_e_ordina_parole(nome_file):
    """Legge un file di testo, elabora le parole e le ordina per frequenza.

    Args:
        nome_file (str): Il nome del file di testo.

    Returns:
        list: Una lista di tuple (parola, frequenza), ordinate per frequenza decrescente.
    """

    parole = leggi_file(nome_file)
    parole_contate = conta_parole(parole)
    parole_ordinate = ordina_parole(parole_contate)
    return parole_ordinate

def leggi_file(nome_file):
    """Legge un file di testo e restituisce una lista di parole.

    Args:
        nome_file (str): Il nome del file di testo.

    Returns:
        list: Una lista di parole.
    """
    with open(nome_file, 'r') as file:
        testo = file.read()
        parole = testo.split()
    return parole

def conta_parole(parole):
    """Conta la frequenza di ciascuna parola in una lista.

    Args:
        parole (list): Una lista di parole.

    Returns:
        dict: Un dizionario dove le chiavi sono le parole e i valori le frequenze.
    """
    conteggio = {}
    for parola in parole:
        conteggio[parola] = conteggio.get(parola, 0) + 1
    return conteggio

def ordina_parole(parole_contate):
    """Ordina le parole in base alla frequenza decrescente.

    Args:
        parole_contate (dict): Un dizionario con le parole e le loro frequenze.

    Returns:
        list: Una lista di tuple (parola, frequenza), ordinate per frequenza decrescente.
    """
    return sorted(parole_contate.items(), key=lambda x: x[1], reverse=True)
'''
secondascomposizione
'''
def leggi_e_ordina_parole(nome_file):
    """(Come sopra)"""

    parole = leggi_file(nome_file)
    parole_pulite = pulisci_testo(parole)
    parole_contate = conta_parole(parole_pulite)
    parole_ordinate = ordina_parole(parole_contate)
    return parole_ordinate

def pulisci_testo(parole):
    """Pulisce una lista di parole rimuovendo punteggiatura e trasformando in minuscolo.

    Args:
        parole (list): Una lista di parole.

    Returns:
        list: Una lista di parole pulite.
    """
    import string
    parole_pulite = []
    for parola in parole:
        parola = parola.strip(string.punctuation).lower()
        if parola:
            parole_pulite.append(parola)
    return parole_pulite
'''
terza scomposizione
'''
import nltk
from nltk.corpus import stopwords

# ... (le altre funzioni rimangono simili)

def pulisci_testo(parole):
    """Pulisce una lista di parole usando NLTK.

    Args:
        parole (list): Una lista di parole.

    Returns:
        list: Una lista di parole pulite.
    """
    stop_words = set(stopwords.words('english'))
    parole_pulite = [parola for parola in parole if parola not in stop_words]
    return parole_pulite
