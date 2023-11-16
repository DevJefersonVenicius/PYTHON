# Números multiplos de 4
# Deletando números multiplos de 4
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_pares = lista[2::2]
print(lista_pares)
del lista[0::4]
print(lista)