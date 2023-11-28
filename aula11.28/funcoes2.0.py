# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721
# pass - para ignorar uma função 
def num_reverso(num):
    reverso = 0
    while num > 0:
        # pegar o ultimo valor do numero
        ultimo_valor = num % 10
        
        # add ultimo numero
        reverso = (reverso * 10) + ultimo_valor
        
        # tira ultimo valor
        num = num // 10
    
    # retorna o reverso
    return reverso

num = int(input('Informe um número: '))
resultado = num_reverso(num)
print(f'O numero informado foi {num} e o reverso dele é: {resultado}')