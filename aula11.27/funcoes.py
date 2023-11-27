# funções são blocos de codigos que são executados somente quando são chamados
# parametro: def
# observação: as funções devem ter prioridade no codigo

def media(nota01, nota02, nota03):
    media = (nota01 + nota02 + nota03) / 3
    
    return media

nota01 = int(input('Informe primeira nota: '))
nota02 = int(input('Informe segunda nota: '))
nota03 = int(input('Informe terceira nota: '))

print(media(nota01, nota02, nota03))

nota04 = int(input('Informe primeira nota: '))
nota05 = int(input('Informe segunda nota: '))
nota06 = int(input('Informe terceira nota: '))

print(media(nota04, nota05, nota06))

def calcula_horas_extras(quanridade_horas, valor_hora):
    horas = float(quanridade_horas)
    taxa = float(valor_hora)

    if horas >= 40:
        valor_receber = (horas - 40) * taxa
    
    return valor_receber

quantidade_horas = float(input('Informe o total de horas trabalhadas: '))
valor_hora = float(input('Informe o valor da taxa do colaborador: '))

print(calcula_horas_extras(quantidade_horas, valor_hora))

salario = 1400.00
print(salario + calcula_horas_extras(quantidade_horas, valor_hora))