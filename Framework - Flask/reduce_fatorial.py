from functools import reduce

def fatorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

numero = 5
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}") 