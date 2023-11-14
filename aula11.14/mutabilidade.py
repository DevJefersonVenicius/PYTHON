# Alguns cuidados com dados mutaveis
# mutaveis - são dados que podem ter seu valor alterado na memoria do dispositivo
# imutaveis - são dados que só podem ser copiados da memoria do dispositivo
lista = ['João', 'Paulo']
lista = ['Francisco', 'Jose']
lista[1] = 'Pedro'
print(lista)
nome = 'Paulo' # seu endereço de memoria é 7e9ritu474j
# nome = 'João'
# print(nome[2])
# nome[2] = 'a'
novo_nome = nome # seu  endereço de  memoria é 9122938477uduf
nome = 'João' # seu endereço de memoria é 7dfjeur8r
print(nome)
print(novo_nome)

lista_a = ['João', 'Paulo'] # endereço de memoria 398dghdjieofk
lista_b = lista_a.copy()
lista_c = lista_b
lista_c[1] = 'Jose'
print(lista_a)
print(lista_b)
print(lista_c)