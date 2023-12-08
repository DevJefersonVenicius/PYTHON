# 6. Faça um quiz utilizando dicionario com as seguintes chaves:  Pergunta, opções, respostas. Faça a validação da opção escolhidada com a resposta e imprima.
perguntas =[
    {'Pergunta': 'Quanto é 5 x 5?',
     'Opções': [12, 16, 20, 25],
     'Resposta': 25,},

    {'Pergunta': 'Quanto é 12 / 4?',
     'Opções': [6, 13, 3, 2],
     'Resposta': 3,},

    {'Pergunta': 'Quanto é 15 + 15?',
     'Opções': [14, 15, 30, 25],
     'Resposta': 30,},
]
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i+1})', opcao)
    print()

    escolha = int(input('Escolha sua opção: '))
    acertou = False

    if escolha == int(pergunta['Resposta']):
        acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou 😔')

    print()

print(f'Você acertou { qtd_acertos } de { len(perguntas) }')