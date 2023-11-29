# estruturas condicionais
variavel = 20
if variavel < 20:
    print('Menor que 20')
elif variavel == 20:
    print('Igual a 20')
elif variavel > 20 and variavel < 50:
    print('Está no entervalo entre 21 e 49')
else: 
    print('Qualque outra coisa')

# estruturas de repetição
# FOR e WHILE

for i in range(1, 10, 2): # impares
    
    print(f'Print o numero {i}')
for i in range(2, 10, 2): # pares
    print(f'Print o numero {i}')

contador = 5
while contador > 0:
    print(f'Esse é o print do número {contador}')
    contador -= 1

# join - unir strings, funciona apenas com strings
lista = ['João', 'Paulo', 'II']
nome = ' '.join(lista)
print(nome)

# monte uma data valida com uma lista 
lista = ['2023', '29', '11']
data = '/'.join(lista)
print(data)