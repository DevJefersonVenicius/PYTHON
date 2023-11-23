# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisivel somente por ele mesmo por 1.
numero = int(input('Informe um numero inteiro: '))
intervalo = range(1, numero + 1)
contador = 0
for i in intervalo:
    if numero % i == 0:
        print(f'Foi divisivel por {i}')
        contador += 1
if contador == 2:
    print(f'O número é primo')