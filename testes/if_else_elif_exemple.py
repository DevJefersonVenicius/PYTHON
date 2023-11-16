nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
nota4 = float(input('Digite sua nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 9:
    print('Você foi aprovado. Parabens!!!')
elif media < 9:
    print('Você ficou de recuperação.')
else:
    media <= 6
    print('Você reprovou.')
print('Sua media foi: ',media)