def contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

meu_contador = contador()
print(meu_contador())  
print(meu_contador())  
print(meu_contador())  