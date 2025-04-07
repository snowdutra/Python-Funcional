def aplicar_operacoes(funcoes, numero):
    return [func(numero) for func in funcoes]

def quadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

def dobro(x):
    return x * 2

funcoes = [quadrado, cubo, dobro]

resultado = aplicar_operacoes(funcoes, 3)
print(resultado) 