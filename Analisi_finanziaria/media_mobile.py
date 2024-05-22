'''
In analisi finanziaria, la media mobile è una misura comune utilizzata per analizzare i prezzi dei titoli nel tempo. 
La media mobile aiuta a smussare le fluttuazioni a breve termine e mettere in evidenza le tendenze a lungo termine. 
La tecnica sliding window è perfetta per calcolare la media mobile.
'''

import pandas as pd

# Supponiamo di avere una serie temporale di prezzi azionari
data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'price': [100, 102, 101, 104, 106, 108, 110, 109, 111, 115]
}
df = pd.DataFrame(data)

# Definisci la finestra (numero di giorni per calcolare la media mobile)
window_size = 3

# Calcola la media mobile usando la tecnica sliding window
df['moving_average'] = df['price'].rolling(window=window_size).mean()

# Stampa il DataFrame con la colonna della media mobile
print(df)

'''
RISULTATO
        date  price  moving_average
0 2023-01-01    100             NaN
1 2023-01-02    102             NaN
2 2023-01-03    101      101.000000
3 2023-01-04    104      102.333333
4 2023-01-05    106      103.666667
5 2023-01-06    108      106.000000
6 2023-01-07    110      108.000000
7 2023-01-08    109      109.000000
8 2023-01-09    111      110.000000
9 2023-01-10    115      111.666667

Applicazioni della media mobile:
Identificazione delle tendenze di mercato: La media mobile aiuta gli analisti a identificare se il mercato sta seguendo una tendenza al rialzo o al ribasso.
Segnali di trading: Gli incroci tra diverse medie mobili (ad esempio, una media mobile a breve termine che incrocia una media mobile a lungo termine) possono essere utilizzati come segnali per comprare o vendere titoli.
Riduzione del rumore: La media mobile riduce il "rumore" nei dati di prezzo, rendendo più facile per gli analisti vedere il quadro generale delle tendenze di prezzo.

'''
