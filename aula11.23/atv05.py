# 5. Faça um programa que peça um nome e imprima quantas vogais tem nesse nome
nome = str(input('Digite um nome: '))
letra0 = 'a'
letra1 = 'A' 
letra2 = 'e'
letra3 = 'E'
letra4 = 'i'
letra5 = 'I'
letra6 = 'o'
letra7 = 'O'
letra8 = 'u'
letra9 = 'U'
print(f'Há {nome.count(letra0)} "a" minusculo nessa frase.')
print(f'Há {nome.count(letra1)} "A" maiusculo nessa frase.')
print(f'Há {nome.count(letra2)} "e" minusculo nessa frase.')
print(f'Há {nome.count(letra3)} "E" maiusculo nessa frase.')
print(f'Há {nome.count(letra4)} "i" minusculo nessa frase.')
print(f'Há {nome.count(letra5)} "I" maiusculo nessa frase.')
print(f'Há {nome.count(letra6)} "o" minusculo nessa frase.')
print(f'Há {nome.count(letra7)} "O" maiusculo nessa frase.')
print(f'Há {nome.count(letra8)} "u" minusculo nessa frase.')
print(f'Há {nome.count(letra9)} "U" maiusculo nessa frase.')