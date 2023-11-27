# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas em graus celsius, e informe ao final a menor e a maior temperaturas informadas. Para sair do programa deve digitar "SAIR"
while True:
    temperatura1 = float(input('Digite a primeira temperatura: '))
    temperatura2 = float(input('Digite a segunda temperatura: '))
    
    if temperatura1 > temperatura2:
        print(f'Essa é a maior temperatura: {temperatura1}')
    if temperatura2 > temperatura1:
        print(f'Essa é a maior temperatura: {temperatura2}')
    if temperatura1 < temperatura2:
        print(f'Essa é a menor temperatura: {temperatura1}')
    if temperatura2 < temperatura1:
        print(f'Essa é a menor temperatura: {temperatura2}')
    if temperatura1 == temperatura2: 
        print('As temperaturas são iguais.')
    
    saida = input('Digite "SAIR" para sair:  ').lower()
    if saida == "sair":
        print(saida.lower())
        print('Você saiu. ')
        break