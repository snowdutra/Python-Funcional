from functools import reduce

compras = [{'quantidade': 2, 'produto': 'banana', 'preço': 1.50},
          {'quantidade': 3, 'produto': 'maçã', 'preço': 2.00},
          {'quantidade': 1, 'produto': 'laranja', 'preço': 1.75},
          {'quantidade': 1, 'produto': 'melão', 'preço': 3.50},
          {'quantidade': 2, 'produto': 'uva', 'preço': 4.00},
          {'quantidade': 4, 'produto': 'pera', 'preço': 2.50}]


# filtre produtos com preço maior que 2.00, gere uma lista com o valor gasto em cada produto e reduza a lista para o total gasto
