"""
Questão 09

• Escreva uma função que calcule o tempo de viagem de uma pessoa lembre de imprmir todos os resultados:

01. peça a distancia e a velocidade media
02. a formula é: distância / velocidade média(hora)
03. não esqueça de limitar a resposta em apenas duas casas decimais 

"""
distancia = float(input('Digite a distância: '))
velocidade_media = float(input('Digite a velocidade: '))
def calcular_tempo_viagem(distancia, velocidade_media):
    tempo_viagem = distancia / velocidade_media
    return int(tempo_viagem)
tempo_resultado = calcular_tempo_viagem(distancia, velocidade_media)
print(f'O tempo de viagem foi de aproximadamente {tempo_resultado} horas.')