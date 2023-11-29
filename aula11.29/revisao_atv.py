# utilizando fatiamento e repetição, imprima uma lista de 'a' até o 'e' removendo uma letra de cada vez
lista = ['a', 'b', 'c', 'd', 'e']
lista_comprimento = len(lista)
for i in range(lista_comprimento):
    print(lista[0:lista_comprimento])
    lista_comprimento -= 1