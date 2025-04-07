# A função map em Python é usada para aplicar uma função a cada item de um iterável (como uma lista) e retornar um iterador com os resultados. Ela é útil para transformar ou processar elementos de uma coleção sem a necessidade de usar loops explícitos.

# Funcionamento:
# Sintaxe: map(funcao, iteravel)
# funcao: A função que será aplicada a cada elemento do iterável.
# iteravel: O iterável cujos elementos serão processados.

palavras = ['python', 'funcional', 'map']

maiúsculas = list(map(lambda palavra: palavra.upper(), palavras))

print(maiúsculas)