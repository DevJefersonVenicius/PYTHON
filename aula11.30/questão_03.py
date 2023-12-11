"""
Questão 03

• Escreva um programa que atenda as requisições abaixo e imprima todos os resultados:

01. imprima quantas vezes aparece a letra "a" no "texto".
02. imprima qual a posição do primeiro "z".
03. leve o "texto" para uma nova variavel e trocando "aprendizado compartilhado" por "vivencia profissional".

"""
texto = "Somos uma escola de tecnologia de informação que cria pontes entre pessoas, conhecimento e empresas. Ambiente que proporciona conexão, troca de conhecimentos e aprendizado compartilhado entre participantes, instrutores e empresas parceiras."
letra = 'a'
print(f'A letra "a" aparece {texto.count(letra)} vezes no texto.')
print(f'A letra "z" está localizada na posição {texto.find("z")}')
texto_atualizado = texto.replace('aprendizado compartilhado', 'vivencia proficional')
print(texto_atualizado)