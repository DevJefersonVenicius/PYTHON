"""
Questão 04

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. crie uma função que faça a troca de caracteres de acordo com a escolha do usuario. Imprima em uma nova string.
02. utilizando um FOR troque os espaços em branco por -.

"""
texto = "Neste curso, os alunos(as) terão capacidades para trabalharem com toda a estrutura de dados que roda por trás de aplicações web. Compreendendo as necessidades de geração, captura e armazenamento de dados de uma aplicação web e a desenvolve, levando sempre em consideração a agilidade, segurança e confiabilidade nos dados que serão gerados e, por vezes, integrados a outros sistemas de gestão estratégica."
def substituir_palavras_e_espacos(texto, palavra_original, palavra_substituta):
    texto_substituido = texto.replace(palavra_original, palavra_substituta)
    return texto_substituido.replace(' ', '-')
palavra_original = input('Digite a palavra a ser substituída: ')
palavra_substituta = input('Digite a palavra substituta: ')
novo_texto = substituir_palavras_e_espacos(texto, palavra_original, palavra_substituta)
print(f'Resultado da substituição de "{palavra_original}" por "{palavra_substituta}" e espaços por "-":\n{novo_texto}')