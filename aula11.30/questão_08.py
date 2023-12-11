"""
Questão 08

• Escreva um programa que atenda as requisições abaixo e imprma todos os resultados:

01. peça três frutas para o usuario e calcule o total da compra dele
02. informe o qual fruta tem o menor valor
03. faça uma promoção e diminua o preco de duas frutas pela metade
04. insira duas novas frutas e seus preços

"""

frutas = ["abacaxi", "uva", "maçã", "abacate", "tangerina"]
precos = [3.50, 4.99, 6.49, 9.10, 4.99]
total_compra = 0
for i in range(3):
    fruta = input("Digite uma fruta: ")
    indice_fruta = frutas.index(fruta)
    total_compra += precos[indice_fruta]
print(f'O total da compra é: R${total_compra}')

menor_valor = min(precos)
indice_menor_valor = precos.index(menor_valor)
fruta_menor_valor = frutas[indice_menor_valor]
print(f'A fruta com o menor valor é: {fruta_menor_valor} com preço de R${menor_valor}')

promocao = ['abacate', 'maçã']
desconto = 0
for fruta in promocao:
    if fruta in frutas:
        indice_fruta = frutas.index(fruta)
        novo_preco = precos[indice_fruta] / 2 
        desconto += precos[indice_fruta] - novo_preco
        desconto_final = total_compra - desconto
print(f'O novo preço a ser pago é de {desconto_final}')

novas_frutas = ["morango", "kiwi"]
novos_precos = [5.99, 7.49]
for i in range(len(novas_frutas)):
    frutas.append(novas_frutas[i])
    precos.append(novos_precos[i])
print(frutas)
print(precos)