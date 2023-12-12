# Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as palavras aparecem COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve utilizar uma lista para realizar a atividade.
# Obs.: você deve validar se a palavra tem três ou mais letras
# Obs.: você deve validar se a frase tem pelo menos 20 palavras

def palavra_completa_frase(palavra, palavra2, palavra3, frase):
    if len(palavra) < 3 or len(palavra2) < 3 or len(palavra3) < 3:
        print('As palavras digitadas devem ter 3 ou mais caracteres.')
        return
    
    elif len(frase) < 20:
        print('A frase digitada deve ter 20 ou mais caracteres.')
        return
    
    lista_frase = list(frase)

    if palavra in frase:
        indice_inicio = frase.find(palavra)
        indice_fim = indice_inicio + len(palavra) - 1
        print(f'A palavra "{palavra}" aparece completa na frase e começa no intervalo de índices {indice_inicio}:{indice_fim} Lista frase: {lista_frase}')
    
    if palavra2 in frase:
        indice_inicio2 = frase.find(palavra2)
        indice_fim2 = indice_inicio2 + len(palavra2) - 1
        print(f'A palavra "{palavra2}" aparece completa na frase e começa no intervalo de índices {indice_inicio2}:{indice_fim2} Lista frase: {lista_frase}')
   
    if palavra3 in frase:
        indice_inicio3 = frase.find(palavra3)
        indice_fim3 = indice_inicio3 + len(palavra3) - 1
        print(f'A palavra "{palavra3}" aparece completa na frase e começa no intervalo de índices {indice_inicio3}:{indice_fim3} Lista frase: {lista_frase}')

    if palavra not in frase and palavra2 not in frase and palavra3 not in frase:
        print('Nenhuma das palavras digitadas está na frase.')

palavra = input('Digite uma palavra: ')
palavra2 = input('Digite uma palavra: ')
palavra3 = input('Digite uma palavra: ')
frase = input('Digite uma frase: ')
palavra_completa_frase(palavra, palavra2, palavra3, frase)