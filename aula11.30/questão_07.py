"""
Questão 07

• Crie uma função que gere uma lista com tuplas em seus elementos, nas tuplas devem conter dois valores nome e idade 

Ex.: [('paulo', 28), ('Jose', 23), ('Roberto', 17)] 

Ainda deve fazer:
• excluir o ultimo valor
• adicionar uma nova tupla no inicio da lista
• Crie uma cópia da lista para não utilizar o mesmo endereço de memoria

"""
lista_nomes = ['João', 'Pedro', 'Mateus', 'Judas', 'Tiago']
lista_idades = [28, 23, 17, 18, 20]
def gerar_lista_tuplas(lista_nomes, lista_idades):
    lista_resultado = []
    for i in range(len(lista_nomes)):
        if i < len(lista_idades):
            tupla = (lista_nomes[i], lista_idades[i])
            lista_resultado.append(tupla)
    return lista_resultado
lista_tuplas = gerar_lista_tuplas(lista_nomes, lista_idades)
print(lista_tuplas)

lista_sem_ultimo_valor = lista_tuplas[:-1]
print(lista_sem_ultimo_valor)

nova_tupla = ('Maria', 30)
lista_com_nova_tupla = [nova_tupla] + lista_tuplas
print(lista_com_nova_tupla)

copia_lista = lista_tuplas.copy()
print(copia_lista)