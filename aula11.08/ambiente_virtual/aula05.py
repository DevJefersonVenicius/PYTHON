# Fatiamento de strings
# Obs: toda string por padrão é uma lista que não saiu do armário
# ordem de tratamento:
# 0123456........
# -654321........
# [i:f:p] = i - INICIO, f - FIM, p - PARSE

nome = "Rodrigo José dos Santos Amaral Neto Junior"
print(nome[0:23])
print(nome[17:23])
print(nome[-6:])
print(nome[1::2])
print(nome[0::3])
print("="*20)
lista_nome = ("J","u","n","i","o","r")
print(nome[3])
print(nome[-2])
print(lista_nome[3])
print(lista_nome[-2])