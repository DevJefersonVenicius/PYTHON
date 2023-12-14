# Obs: toda vez que criar uma classe deve-se separar os metodos por categoria
class Automovel:
    def __init__(self, placa, cor):
        self.__placa = placa
        self.__cor = cor

    def get_placa(self):
        return self.__placa
    
    def get_cor(self):
        return self.__cor
    
    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade}Km/h')

carro = Automovel('TYV-0019', 'azul')
moto = Automovel('GJG-1716', 'preta')
caminhao = Automovel('KHZ-8970', 'vermelha')

# Chamadas GET
print(f'A placa do carro é: {carro.get_placa()}')
print(carro.dirigir(220))
print(f'A placa da moto é: {moto.get_placa()}')
print(moto.dirigir(90))
print(f'A placa do caminhão é: {caminhao.get_placa()}')
print(caminhao.dirigir(70))

print('='*20)

# Novas chamadas GET
print(f'A nova cor do carro é {carro.get_cor()}')
print(f'A nova cor da moto é {moto.get_cor()}')
print(f'A nova cor do caminhão é {caminhao.get_cor()}')

print('='*20)

# Chamadas SET
carro.set_cor('branca')
moto.set_cor('amarela')
caminhao.set_cor('verde')
print(f'A nova cor do carro agora é {carro.get_cor()}')
print(f'A nova cor da moto agora é {moto.get_cor()}')
print(f'A nova cor do caminhão agora é {caminhao.get_cor()}')