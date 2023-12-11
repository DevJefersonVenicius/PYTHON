"""
Questão 10

• Escreva uma função que calcule o fatorial de um numero e lembre de imprimir todos os resultados:

01. o numero  deve ser solicitado ao usuario

"""
def calcular_fatorial(numero):
    if numero < 0:
        return
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)
numero = int(input('Digite um número para calcular o fatorial: '))
resultado_fatorial = calcular_fatorial(numero)
print(f'O fatorial de {numero} é {resultado_fatorial}.')