# faça um programa que leia 10 numeros e diga a quantidade de pares e impares
contador_par = 0
contador_impar = 0
for i in range(1, 11):
    numero = int(input(f'Digite o {i}° numero: '))
    if numero % 2 == 0:
        contador_par += 1
    else: 
        contador_impar += 1
print(f'A quantidade de numeros pares é: {contador_par}')
print(f'A quantidade de numeros impares é: {contador_impar}')