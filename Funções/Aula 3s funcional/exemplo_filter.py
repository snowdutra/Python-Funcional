compras = [{'quantidade': 2, 'produto': 'banana', 'preço': 1.50},
          {'quantidade': 3, 'produto': 'maçã', 'preço': 2.00},
          {'quantidade': 1, 'produto': 'laranja', 'preço': 1.75}]


# lista_maiores = []

# for item in compras:
#     if item['preço'] > 1.5:
#         lista_maiores.append(item)

# print(lista_maiores)


# # 1 funcional com filter e definição de função

print(filter(lambda item: item['preço'] > 1.5, compras))
print(list(filter(lambda item: item['preço'] > 1.5, compras)))

