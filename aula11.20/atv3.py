# faça um codigo que leia 5 números e informe o maior número
while True:
    num = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    num3 = float(input('Digite o terceiro número: '))
    num4 = float(input('Digite o quarto número: '))
    num5 = float(input('Digite o quinto número: '))
    if num > num2 and num > num3 and num > num4 and num > num5:
        print(f'O maior número é: {num}')
    if num2 > num and num2 > num3 and num2 > num4 and num2 > num5:
        print(f'O maior número é: {num2}')
    if num3 > num and num3 > num2 and num3 > num4 and num3 > num5:
        print(f'O maior número é: {num3}')
    if num4 > num and num4 > num2 and num4 > num3 and num4 > num5:
        print(f'O maior número é: {num4}')
    if num5 > num and num5 > num2 and num5 > num3 and num5 > num4:
        print(f'O maior número é: {num5}')
        break