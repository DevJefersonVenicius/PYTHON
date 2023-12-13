# Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as palavras aparecem COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve utilizar uma lista para realizar a atividade.
# Obs.: você deve validar se a palavra tem três ou mais letras
# Obs.: você deve validar se a frase tem pelo menos 20 palavras

def palavra_completa_frase(palavra, frase):
    
    if len(palavra) < 3:
        print('As palavras digitadas devem ter 3 ou mais caracteres.')
        return
    
    if len(frase) < 20:
        print('A frase digitada deve ter 20 ou mais caracteres.')
        return
    
    if palavra in frase: 
        indice_palavra = frase.index(palavra) - 1
        indice_fim_palavra = indice_palavra + len(palavra) + 1
        print(f'A palavra "{palavra}" está completa no texto. No intervalo de indices {indice_palavra}:{indice_fim_palavra}')

    if palavra2 in frase:
        indice_palavra2 = frase.index(palavra2) - 1
        indice_fim_palavra2 = indice_palavra2 + len(palavra2) + 1
        print(f'A palavra "{palavra2}" está completa no texto. No intervalo de indices {indice_palavra2}:{indice_fim_palavra2}')
    
    if palavra3 in frase: 
        indice_palavra3 = frase.index(palavra3) - 1
        indice_fim_palavra3 = indice_palavra3 + len(palavra3) + 1
        print(f'A palavra "{palavra3}" está completa no texto. No intervalo de indices {indice_palavra3}:{indice_fim_palavra3}')
    
    if palavra not in frase:
        print('Nenhuma das palavras digitadas está na frase.')

palavra = input('Digite uma palavra: ')
palavra2 = input('Digite uma palavra: ')
palavra3 = input('Digite uma palavra: ')
palavras_lista = [palavra, palavra2, palavra3]
print(palavras_lista)
frase = input('Digite uma frase: ')
palavra_completa_frase(palavra, frase)