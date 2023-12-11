"""
Questão 02

• Escreva um programa que, recebe uma palavra e uma frase, crie uma função que verifique se as letras da palavra aparecem na frase, e quantas vezes aparecem. Imprima os resultados.

Obs: você deve validar se a palavra tem três ou mais letras
Obs: você deve validar se a frase tem pelo menos 25 caracteres

Exemplos do resultado:
    palavra = "pato" 
    frase = "a capa do livro velho"
    P aparece 1 vez
    A aparece 3 vezes
    T não aparece
    O aparece três vezes
"""
def verificar(palavra, frase):
    if len(palavra) < 3:
        print('A palavra digitada deve ter 3 ou mais caracteres.')
        return
    if len(frase) < 25:
        print('A palavra digitada deve ter 25 caracteres.')
        return
    for letra in set(palavra):
        set(frase)
        if letra in palavra and letra in frase:
            indice_palavra = palavra.index(letra)
            indice_frase = frase.index(letra)
            print(f'{letra} aparece {indice_palavra + indice_frase} vezes')

palavra = input('Digite uma palavra: ')
frase = input('Digite uma frase: ')
verificar(palavra, frase)