# Listar os pares do nomes
# Remover o nomes multiplos de 3
nomes = ['João', 'Sergio', 'Vitor', 'Manel', 'Rogerio', 'Roberval', 'Caio', 'Jose', 'Amanda', 'Lais', 'Gabriel']
#          0        1         2       3         4          5           6      7        8        9        10
lista_pares = nomes[1::2]
print(lista_pares)
del nomes[0::3]
print(nomes)