def soma_recursiva(n):
    if n == 1: 
        return 1
    return n + soma_recursiva(n - 1)

numero = 5
resultado = soma_recursiva(numero)
print(f"A soma dos números de 1 a {numero} é {resultado}")