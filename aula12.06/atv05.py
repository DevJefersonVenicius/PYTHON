# 5. Vamos criar um sistema de login e senha. Crie um dicionario contendo os acessos dos colaboradores com nome de usuario e senha. Em seguida peça as informações e valide o login do usuario.
dic_acessos = {'Jeferson': '12345', 'João': '121212'}

user = input('Informe seu USUARIO: ')
password = input('Informe sua SENHA: ')

user_password = {}
user_password[user] =  password

for chave in dic_acessos.keys():
    if chave == user:
        if dic_acessos[chave] == user_password[user]:
            print('Acesso liberado')
            break
        else:
            print(f'Senha incorreta para o usuario {user}')
            break
    else:
        print(f'O usuario {user} não foi encontrado')
        break
else: 
    print('Usuario incorreto')