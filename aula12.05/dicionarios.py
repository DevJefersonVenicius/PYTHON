# Possuem CHAVE(KEYS) e VALOR(VALUES)
# parametro: {} ou dict()
# o valor pode se repitir mas a chave não
# chaves repitidas não são contabilizadas sendo apenas contabilizada uma
# pop - para usar no dicionario deve-se dizer a chave a ser deletada
# update - dicionarios só podem ser atualizados com dicionarios

pessoa = {'nome': 'Paulo', 'sobrenome': 'Junior', 'nome 2': 'Rodrigo', 'sobrenome': 'Junior 2', 'sobrenome 4': 'Junior', 'idade': '23',}
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())

k = pessoa.keys()
print(k)
v = pessoa.values()
print(v)

for chave in k:
    print(chave)

print('='*20)

for chave in v:
    print(chave)

print('='*20)

for chave in pessoa.values():
    print(chave)

for chave, valor in pessoa.items():
    print(chave, valor)

i = pessoa.items()
print(i)

print('='*20)

print(pessoa['sobrenome 4']) # para imprimir o valor de uma chave especifica
print(pessoa['sobrenome'])
print(pessoa['idade'])

print('='*20)

d1 = {'valor 1': 100, 'valor 2': 200, 'valor 3': 300,}

d2 = d1.copy()

print(d1)

d2['valor 2'] = 2000

print(d1)

print(type(d2))

print(d2)

print(d2.get('valor 2'))

print('='*20)

d3 = d1.pop('valor 3')

print(d1)

outro_nome = {'valor 4': 5, 'valor 6': 6}

d1.update(outro_nome)

print(d1)