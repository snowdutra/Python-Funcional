from functools import reduce

def progressao_aritmetica(n):
    return reduce(lambda acc, x: acc + [acc[-1] + 1], range(n), [0])

n = 10
resultado = progressao_aritmetica(n)
print(resultado)