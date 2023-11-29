variavel = 1

print(variavel)

variavel = 'ABCDEFGHIJK'
#           012345678910
# -11-10-9-8-7-6-5-4-3-2-1
print(variavel)

# regra do fatiamento [inicio, fim, step/parse]

print(variavel[::-1])
print(variavel[0:5])

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#         0    1    2    3    4    5    6
#        -7   -6   -5   -4   -3   -2   -1
print(lista[::-1])
print(lista[1:5])

for i in range(1, 6):
    i = lista[0:5]
    i = lista[1:5]
    i = lista[2:5]
    i = lista[3:5]
    i = lista[4:5]
    print(i)
    break