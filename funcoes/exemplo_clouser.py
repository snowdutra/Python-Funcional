def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == "__main__":
    triplo = multiplicar(3)
    print(triplo)
    print(triplo(8))
