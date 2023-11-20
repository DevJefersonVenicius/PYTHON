# faça um codigo que leia um nome de usuario e a sua senha e não aceite a senha igual ao nome do usuario, mostrando uma mensagem de erro pedindo as informações novamente.
while True:
    nome = input('Qual o nome? ')
    senha = input('Qual a senha: ')
    if nome == senha:
        print('ERROR')
    if nome != senha:
        print('Correto')
        break