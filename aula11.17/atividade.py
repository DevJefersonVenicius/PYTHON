contador = 0
while contador < 20:
    idade_aluno = int(input('Informe sua idade: '))
    if idade_aluno > 13:
        print(f'O aluno {contador} tem mais de 13 anos')
contador += 1