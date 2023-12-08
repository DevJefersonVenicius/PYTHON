# 3. Faça um codigo que pede a marca e o modelo do carro do cliente insere ele em uma lista e depois transforma em um dicionario. Imprima os dois resultados.
marca = input('Digite a marca de sua preferencia: ')
modelo = input('Digite o modelo: ')

lista = []
lista.insert(0, marca)
lista.insert(1, modelo)
print(lista)

dic = {}
dic.update([lista])
print(dic)

dic['Fiat'] = 'Uno' # outra forma de adicionar itens
print(dic)