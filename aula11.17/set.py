# Set - Conjuntos
# para criar um set com duas ou mais variaveis, use chaves {}
# o set não garante ordem
set01  = set('Paulo')
set02 = {'Paulo', 'Junior', 'Lara', 'Kaynan', 'Felipe'}
print(set01)
print(set02)

lista = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5]
print(lista)
set03 = set(lista)
print(set03)
print(7 not in set03)
print(5 not in set03)

for i in set03:
    print(i)

set03.add('João')
set03.add(6)
set03.update('Paulo')
set03.discard('Paulo')
set03.clear()
print(set03)

set04 = {1, 2, 3, 4, 5}
set05 = {4, 5, 6, 7, 8}

set06 = set04 | set05 # união de conjuntos
print(set06)
set06 = set04 & set05 # interceção de conjuntos
print(set06)
set06 = set05 - set04 # diferenças dos conjuntos
print(set06)