def executar(func, numero):
    return func(numero)

def quadrado(x):
    return x ** 2

resultado = executar(quadrado, 5)
print(resultado)