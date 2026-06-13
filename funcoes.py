def exponencial(expoente, base=2.71):
    resultado=0
    x=1
    fatoriais=fatorial(10)
    for i in range(10):
        x=-expoente*x
        y=(x)/fatoriais[i]
        z=y
        resultado+=z
        resultado=round(resultado,5)
    return resultado