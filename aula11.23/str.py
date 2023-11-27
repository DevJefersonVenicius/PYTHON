# count - funçao é contar quantas vezes um determinado caractere aparece em uma string
# upper e a lower - dois metodos que deixam a string toda em maiuscula ou a string toda em minuscula
# find - busca por uma espressão dentro da frase
# replace  - é utilizado para realizar alterações dentro das strings
# capitalize - deixa a primeira letra da frase maiuscula
# split - transforma sua string em uma lista
frase = "a banana é amarela e o abacate é verde.".lower()
letra = 'a'
email = ' veniciusvieira90@gmail.com '
print(f'A letra "{letra}" aparece {frase.count(letra)} vezes na frase "{frase}"')
achei = frase.find(' a')
if achei >= 0:
    print(f'A expressão foi encontrada no indice {achei}')
else:
    print(f'A expressão NÃO foi encontrada na frase')

saida = input('Digite "S" para sair: ').lower()
if saida == "s":
    print(saida.lower())

nova_frase = frase.replace('banana', 'maracuja')
nova_frase2 = frase.replace('banana', 'manga')
nova_frase2 = frase.replace(' ', '')

print(frase)
print(nova_frase)
print(nova_frase2)
print(email.replace(' ', ''))
print(frase.capitalize())
print(frase.split())