total_de_tentativas = 0
nivel = int(input("Qual o nivel? "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
print(f'O total de Tentativas é igual a: {total_de_tentativas}')