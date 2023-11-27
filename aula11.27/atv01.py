# Faça um programa, com uma função que nescessite de um argumento. A função retorna o valor de caractere 'P', se seu argumento for positivo, e 'N', se seu argumento for zero ou negativo.
def funcao(arg):
    argumento = int(arg)
    if arg > 0:
      funcao = "P"
    else: 
        funcao = "N"
    return funcao
arg = int(input('Digite um numero: '))
print(funcao(arg))