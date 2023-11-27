# 7. Faça um programa que peça uma palavra e a imprima de tras-pra-frente
nome = str(input('Digite um nome: '))
for i in range(len(nome) -1, -1, -1):
    print(nome[i])