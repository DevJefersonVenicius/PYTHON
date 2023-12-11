"""
Questão 05

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. monte um conjunto(SET) com o nome "meu_conjunto1", nele você deve colocar os indices impares da "minha_lista"
02. transforme a "minha_lista" em uma string separada por /
03. monte uma lista iversa da "minha_lista"
04. informe quanntos elementos estão contidos em "minha_lista" e quantos estão contidos em "meu_conjunto"

"""

minha_lista = ["com", "um", "notebook", "e", "internet", "de", "banda", "larga", "qualquer", "jovem", "capacitado", "poderá", "trabalhar", "ou", "empreender", "do", "Ceará", "para", "o", "Brasil", "e", "o", "mundo", "e", "consequentemente", "transformando", "a", "sua", "vida", "e", "aquecendo", "a", "economia", "local"]
meu_conjunto1 = set(minha_lista[1::2])
print(meu_conjunto1)

print('='*20)

minha_string = '/'.join(minha_lista)
print(minha_string)

print('='*20)

lista_inversa = minha_lista[::-1]
print(lista_inversa)

print('='*20)

print(f'Há {len(minha_lista)} elementos na lista.')
print(f'Há {len(meu_conjunto1)} elementos no conjunto.')