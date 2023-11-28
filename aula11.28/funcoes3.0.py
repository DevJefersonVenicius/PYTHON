# Faça uma função que informe a quantidade de digitos de um determinado numero inteiro.
def quantidade(num):
    quantidade = len(num)
    return quantidade

num = (input('Digite um numero: '))    
print(f'Há {quantidade(num)} digitos nesse numero.')