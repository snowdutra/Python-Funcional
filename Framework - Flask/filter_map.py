numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados_impares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numeros)))

print(quadrados_impares) 