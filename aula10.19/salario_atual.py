salario_atual = float(input('Digite seu salario atual: '))
reajuste = float(input('Digite o reajuste % para o novo salario: '))
print(f'O novo salario de acordo com o reajuste de {reajuste} é igual a: ', (salario_atual * reajuste /100) + salario_atual)