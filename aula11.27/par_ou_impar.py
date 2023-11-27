jogador1 = (input('Escolha par ou impar: ')).lower()
jogador2 = ...
if jogador1 == 'par':
   jogador2 == 'impar'
else:
   jogador2 = 'par'

numero_jogador1 = int(input('Escolha seu número: '))
numero_jogador2 = int(input('Escolha seu número: '))

resultado = numero_jogador1 + numero_jogador2
if resultado % 2 == 0:
   if jogador1 == 'par':
      print('Jogador1. You Win!!!')
   else:
      print('Jogador2. You Win!!!')
else:
   if jogador1 == 'impar':
      print('Jogador1. You Win!!!')
   else:
      print('Jogador2. You Win!!!')