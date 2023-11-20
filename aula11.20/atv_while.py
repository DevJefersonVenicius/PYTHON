# Faça um codigo que peça uma nota, entre 0 e 10. Mostre uma mensagem caso a nota seja invalida e continue pedindo até que o usuário infomre uma nota válida.
while True:
    nota = float(input('Informe a nota: '))
    if nota < 0 or nota > 10:
        print('Nota invalida. ')
    if nota >= 0 and nota <= 10:
        print('Nota valida. ')
        break