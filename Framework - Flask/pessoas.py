from functools import reduce

# Lista fornecida
pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17}
]

menores_de_18 = filter(lambda pessoa: pessoa['idade'] < 18, pessoas)

idades = map(lambda pessoa: pessoa['idade'], menores_de_18)

soma_idades = reduce(lambda acumulador, idade: acumulador + idade, idades)

print(soma_idades)