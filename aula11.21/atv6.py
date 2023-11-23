# Faça um programa que peça para 10 pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 a 60 e maior que 60; e então, dizer se a turma é jovem ou adulta ou idosa, conforme a média calculada
soma_idades = 0
for i in range(10):
    idade_pessoas = int(input('Digite a idade: '))
    soma_idades += idade_pessoas
media = soma_idades / 3
if media <= 25:
    print('A media é maior para Jovens') 
elif media == 26 or media <= 60:
    print('A media é maior para Adultos')
else:
    media >= 60 
    print('A media é maior para Idosos')