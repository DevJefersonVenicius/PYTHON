# Escreva uma função chamada gorjeta, que recebe o valor da conta de um restaurante, calcula e exibe a gorjeta do garçom, considerando 12% do valor da conta.
def gorjeta(valor_conta):
    gorjeta = valor_conta * 0.12
    return gorjeta
valor_conta = float(input('Digite o valor: '))
print(f'A gorjeta do garçom foi de {gorjeta(valor_conta)} R$')