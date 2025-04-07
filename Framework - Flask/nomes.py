lista = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

frases = list(map(lambda pessoa: f"{pessoa['nome']} tem {pessoa['idade']} anos.", lista))

print(frases)