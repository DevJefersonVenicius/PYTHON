# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas em graus celsius, e informe ao final a menor e a maior temperaturas informadas. Para sair do programa deve digitar "SAIR"
while True:
    temperatura1 = float(input('Digite a primeira temperatura: '))
    temperatura2 = float(input('Digite a segunda temperatura: '))
    maior = temperatura1 > temperatura2 or temperatura2 > temperatura1
    menor = temperatura1 < temperatura2 or temperatura2 < temperatura1
    if maior:
        print(maior)
    if menor:
        print(menor)