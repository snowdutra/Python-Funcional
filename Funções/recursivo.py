def fatorial_imperativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado    

def fatorial(n):
    return n * (fatorial(n - 1) if (n-1) > 0 else 1)

if __name__ == '__main__':
    print(fatorial_imperativo(5))
    print(fatorial(5))