def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2

if __name__ == "__main__":
    x = 42
    d = dobro
    q = quadrado
    print(d(10)) # Saída: 20
    print(q(10)) # Saída: 100
    print(quadrado(dobro(3)))
    print(q(d(8)))

