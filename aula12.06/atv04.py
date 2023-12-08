# 4. Crie um cadastro de clientes, recebendo nome, idade, data de aniveersario e endereço completo(rua, numero da residencia e bairro). Adicione todas as informações em um dicionario. Imprima  ao final.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
data_aniversario = input('Digite sua data de aniversário: ')
rua = input('Digite a rua: ')
numero_residencia = input('Digite o número da residência: ')
bairro = input('Digite o bairro: ')

informacoes = {'nome': nome, 'idade': idade, 'data_aniversario': data_aniversario, 'rua': rua, 'numero_residencia': numero_residencia, 'bairro': bairro}

lista_informacoes = [informacoes]
print(lista_informacoes)

dic_informacoes = {}
for informacao in lista_informacoes:
    dic_informacoes.update(informacao)

print(dic_informacoes)