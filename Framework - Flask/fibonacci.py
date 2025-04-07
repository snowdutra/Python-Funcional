from functools import reduce

def fibonacci(n):
    return reduce(lambda acc, _: acc + [acc[-1] + acc[-2]], range(n - 2), [1, 1])

resultado = fibonacci(10)
print(resultado)