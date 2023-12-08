# CRUD - Created, Readed, Updated e Deleted

dic = {'Nome': 'Paulo',}# Created
print(dic)
dic2 = dict(Idade=23) # Created
print(dic2)
dic['Nome'] # Readed
print(dic)
dic2.get('Idade') # Readed
print(dic2)
dic.update(sobrenome='Junior') # Updated
print(dic)
dic.update({'Idade': 23}) # Updated
print(dic)
tupla = ('peso', 72.12), # para adicionar uma tupla ou lista deve colocar uma virgula após fechar o item
dic.update(tupla) # Updated
print(dic)
lista = ['data', '13/04/1996'], ['numeros', [1, 2, 3, 4, 5, 6, 7, 8, 9,]] # pode-se adicionar dois
dic.update(lista) # Updated
print(dic)
dic.clear() # Deleted
print(dic)