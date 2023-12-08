# 1. Crie uma lista de alunos com nome e nota final de cada aluno e coloque em um dicioario, depois imprima.

alunos_notas = [['João', 8], ['José', 9], ['Roger', 7], ['Lais', 10]]
dic = {}
dic.update(alunos_notas)
print(dic)

# 2. Ainda sobre a questão 1. Insira mais 04 alunos e notas no seu dicionario.

dic.update(Vitoria=10, Maria=7, Venicius=8, Vitor=5)
print(dic)