'''
Nel nostro esempio, la funzione f è una semplice parabola, e cerchiamo il punto di massimo all'interno dell'intervallo [0, 6]. Una volta trovato il punto di massimo, stampiamo il valore del punto e il valore massimo della funzione in quel punto.
'''
def ternary_search(f, l, r, eps):
    while abs(r - l) > eps:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        if f(m1) < f(m2):
            l = m1
        else:
            r = m2
    return (l + r) / 2
