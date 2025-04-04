compras = [{'quantidade': 2, 'produto': 'banana', 'preço': 1.50},
          {'quantidade': 3, 'produto': 'maçã', 'preço': 2.00},
          {'quantidade': 1, 'produto': 'laranja', 'preço': 1.75}]



# # estruturada
# total = 0.0
# for item in compras:
#     total += item['quantidade'] * item['preço']


# print(f'Total: {total}')


# # 1 funcional com map e definição de função
# def calculapreco(item):
#     return item['quantidade'] * item['preço']

# print(list(map(calculapreco, compras)))


# 2 funcional com map e lambda
print(list(map(lambda item: item['quantidade'] * item['preço'], compras)))