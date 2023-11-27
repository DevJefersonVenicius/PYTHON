# Supondo que a população de um país A seja de 80000 habitantes com uma taxa anual de crescimento de 3% Faça um programa que calcule e escreva o número de anos necessários para que a população do país A chegar a 120000 habitantes
populacao_atual = 80000
crescimento_anual = 0.3
populacao_final = 120000
contador = 0
while True:
    calculo = (populacao_atual * crescimento_anual) + populacao_atual
    print(calculo)
    contador += 1
    populacao_atual = calculo
    if calculo >= populacao_final:
        print(f'Levou cerca de {contador} anos para chegar a {populacao_final} habitantes. ')
        break