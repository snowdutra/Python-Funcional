def multiplicador(n):
    return lambda x: x * n

multiplica_por_3 = multiplicador(3)
resultado = multiplica_por_3(10)
print(resultado)