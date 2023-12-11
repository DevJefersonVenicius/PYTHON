"""
Questão 01

• Escreva um programa que, recebe uma palavra, crie uma função que verifica na lista "alfabeto" a que indice pertence cada letra da palavra. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: letras repetidas devem ser verificadas somente uma vez

Exemplos do resultado:
    palavra = "cidade" 
    C está no indice 2
    I está no indice 8
    D está no indice 3
    A está no indice 0
    E está no indice 4
"""

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z' ]

def encontrar_letras_indice(palavra):
    alfabeto
    for indice, letra_alfabeto in enumerate(alfabeto):
        for i, letra_palavra in enumerate(set(palavra)):
            if letra_alfabeto == letra_palavra:
                print(f'{letra_palavra} aparece no índice {indice}')

palavra = input('Digite uma palavra: ')
encontrar_letras_indice(palavra)