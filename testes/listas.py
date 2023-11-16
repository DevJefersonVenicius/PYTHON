# 1. mostre o total de itens da lista
# 2. fatiamento - monte um sanduiche
# 3. fatiamento - faça uma lista em ordem alfabetica
# 4. fatiamento - faça uma lista em ordem alfabetica contraria
# 5. delete - delete os três alimentos do meio, imprima uma lista
# 6. remova - remova o primeiro e o ultimo, remova o penultimo e o segundo, imprima uma lista 
# 7. adicione dois itens a nova lista
# 8. remova o ultimo item usando o pop
# 9. insira um novo item no inicio
# 10. mostre o novo total de itens
compras = ['Pão', 'Leite', 'Ovos', 'Farinha', 'Feijão', 'Queijo', 'Arroz', 'Macarrão', 'Alface', 'Carne', 'Tomate']

print(len,(compras))

print('='*20)

sanduiche = [compras[0], compras[2], compras[5], compras[8], compras[10]]
print(sanduiche)

print('='*20)

ordem_alfabetica = [compras[-3], compras[-5], compras[-2], compras[3], compras[-7], compras[1], compras[-4], compras[2], compras[0], compras[-6], compras[-1]]
print(ordem_alfabetica)

print('='*20)

ordem_contraria = [compras[-1], compras[-6], compras[0], compras[2], compras[-4], compras[1], compras[-7], compras[3], compras[-2], compras[-5], compras[-3]]
print(ordem_contraria)

print('='*20)

del compras[4]
del compras[-6]
del compras[-5]
print(compras)

print('='*20)

compras.remove('Pão')
compras.remove('Tomate')
compras.remove('Carne')
compras.remove('Leite')
print(compras)

print('='*20)

compras.append('Cuscuz')
compras.append('Tapioca')
print(compras)

print('='*20)

compras.pop(-1)
print(compras)

print('='*20)

compras.insert(0, "Batata")
print(compras)

print('='*20)

print(len,(compras))

