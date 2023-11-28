# condição ternaria acontece em formato de linha

salario = float(input('Informe o valor do seu salario: '))

if salario >= 2500.00:
    print('IR será cobrado')
else:
    print('IR não será cobrado')

variavel_controle = 'IR será cobrado' if salario >= 2500.00 else 'IR não será cobrado' 
print(variavel_controle)

vr_controle = 'OK 1' if False else 'OK 2' if True else 'Fim'
print(vr_controle)

if False:
    print('OK 1')
elif False:
    print('OK 2')
else:
    print('Fim')