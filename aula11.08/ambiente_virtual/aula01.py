nome = "Jeferson"
altura = 1.90
peso = 96
imc = peso / (altura * altura)
# Três pontos "..."" é um valor ainda indefinido
exemplo = ...
# A reposta dessa questão deve ser:
# FULANO tem ALT de altura, pesa PES quilos e seu  imc é:
# VALOR

print(nome, "tem", altura, "de altura")
print("Pesa", peso, "quilos e seu IMC é:")
print(imc)

print(f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu imc é: ')
print(f'{imc:.2f}')