# for trabalha com interaveis
# tem que possuir uma variavel de controle
# inter()
#  next()

#nome = 'Paulo'
#print(next(letra))
#print(next(letra))
#print(next(letra))
#print(next(letra))
#print(next(letra))
#print(letra)
#for letra in nome:
#    print('Ok')

print('='*20)

lista_nomes = ['João', 'Pedro', 'Mateus', 'Judas', 'Tiago']

print(lista_nomes)

lista_enumerada = enumerate(lista_nomes)
print(lista_nomes)
print(list(lista_enumerada))

for item in lista_enumerada:
    print(item)

for indice_lista, item_lista in enumerate(lista_nomes):
    print(f'{item_lista} é o {indice_lista} da lista')