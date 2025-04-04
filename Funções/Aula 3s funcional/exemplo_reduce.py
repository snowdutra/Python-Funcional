from functools import reduce

compras = [{'quantidade': 2, 'produto': 'banana', 'preço': 1.50},
          {'quantidade': 3, 'produto': 'maçã', 'preço': 2.00},
          {'quantidade': 1, 'produto': 'laranja', 'preço': 1.75}]

# quantidade = 0  
# for item in compras:
#     quantidade += item['quantidade']

# print(quantidade)


quantidade_total = reduce(lambda total, item: total + item['quantidade'], compras, 0)
print(quantidade_total)