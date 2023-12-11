"""
Questão 06

• Escreva um programa que atenda as requisições abaixo e imprma todos os resultados:

01. crie uma nova lista só com os numeros pares.
02. crie uma nova lista só com os numeros impares.
03. crie uma nova lisa só com os multiplos de 2.
04. some todos os itens da "lista" 
05. informe quais valores se repetem

"""

lista = [10,11,20,22,30,33,40,11,50,55,60,66,70,22,80,88,90,99]
lista_pares = lista[0::2] + [lista[3]] + [lista[-3]] + [lista[-5]] + [lista[-7]]
print(lista_pares)
lista_impares = [lista[1]] + [lista[5]] + [lista[7]] + [lista[9]] + [lista[-1]]
print(lista_impares)
lista_multiplos_de_2 = lista[::2] + [lista[3]] + [lista[-5]] + [lista[-7]] + [lista[-3]]
print(lista_multiplos_de_2)
soma_total = 0
for elemento in lista:
    soma_total += elemento
print(f'A soma de todos os itens da lista é de: {soma_total}')
print(f'O {lista[3]} se repete {lista.count(22)} vezes e o {lista[7]} se repete {lista.count(11)} vezes.')