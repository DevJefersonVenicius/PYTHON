# Operadores IN e NOT IN

nome = "Paulo Junior"
print( 'ulo J' in nome)

print('='*20)

seu_nome = input('Informe seu nome: ')
buscar = input('Informe o valor a ser encontrado: ')

if ( buscar in seu_nome ):
    print(f'{ buscar } está contido { seu_nome }')
else:
    print(f'{ buscar } NÃO está contido em { seu_nome }')

nao_nome = "Joãozinho"
print("au" not in nao_nome)
# continuar depois
nao_nome2 = input('Informe seu nome: ')
buscar = input('Informe o valor a ser encontrado: ')

if ( buscar in seu_nome ):
    print(f'{ buscar } está contido { seu_nome }')
else:
    print(f'{ buscar } NÃO está contido em { seu_nome }')