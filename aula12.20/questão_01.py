"""
Questão 01

• Faça a abstração da superclasse Veículo. Você deve ter pelo menos duas subclasses, nove atributos e 12 metodos.

Obs: você deve fazer o str de cada uma delas

------------------
|    Veiculos    |
------------------

"""
class Veiculos:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.__placa = None
        self.freio = 0
        self.acelerador = 0
        self.farol = False
        self.pneu = None
        self.portas = 4
        self.ligada = False
        self.freiagem = False

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_cor(self):
        return self.cor

    def get_placa(self):
        return self.__placa

    def get_freio(self):
        return self.freio

    def get_acelerador(self):
        return self.acelerador

    def get_farol(self):
        return self.farol

    def get_pneu(self):
        return self.pneu

    def get_portas(self):
        return self.portas

    def set_marca(self, nova_marca):
        self.marca = nova_marca

    def set_modelo(self, meu_modelo):
        self.modelo = meu_modelo

    def set_cor(self, minha_cor):
        self.cor = minha_cor

    def set_placa(self, minha_placa):
        self.__placa = minha_placa

    def set_farol(self, meu_farol):
        self.farol = meu_farol

    def set_pneu(self, meu_pneu):
        self.pneu = meu_pneu

    def set_portas(self, minhas_portas):
        self.portas = minhas_portas

    def __str__(self):
        return f"Veículo {self.marca} {self.modelo} de cor {self.cor}"

    def valida_ligada(self):
        if self.ligada == True:
            return 'Ligado(a)'
        else:
            return 'Desligado(a)'

class Moto(Veiculos):
    def __init__(self, marca, modelo, cor, placa):
        super().__init__(marca, modelo, cor)
        self.set_placa(placa)

    def trocar_pneu(self):
        self.pneu = 2
        return 'Trocando pneu da moto'

    def encher_pneu(self):
        self.pneu = 2
        return 'Enchendo os pneus da moto'

    def aumentar_acelerador(self):
        self.acelerador += 1
        return 'Acelerando'

    def diminuir_acelerador(self):
        self.acelerador -= 1
        return 'Desacelerando'

    def valida_acelerador(self):
        if self.acelerador >= 0:
            return f'Acelerador em {self.acelerador}'
        else:
            return 'Acelerador em 0%'

    def __str__(self):
        return f'Moto {super().__str__()}'

class Carro(Veiculos):
    def __init__(self, marca, modelo, cor, placa):
        super().__init__(marca, modelo, cor)
        self.set_placa(placa)

    def ligar(self):
        self.ligada = True
        return 'Carro ligado'

    def desligar(self):
        self.ligada = False
        return 'Carro desligado'

    def trocar_pneu(self):
        self.pneu = 4
        return 'Trocando pneu do carro'

    def encher_pneu(self):
        self.pneu = 4
        return 'Enchendo os pneus do carro'

    def aumentar_acelerador(self):
        self.acelerador += 1
        return 'Acelerando'

    def diminuir_acelerador(self):
        self.acelerador -= 1
        return 'Desacelerando'

    def abrir_capota(self):
        return 'Abrindo capota'

    def fechar_capota(self):
        return 'Fechando capota'

    def valida_acelerador(self):
        return f'Acelerador em {self.acelerador if self.acelerador >= 0 else 0}%'

    def __str__(self):
        return f'Carro {super().__str__()}'

moto_user = Moto('Honda', 'CG-150', 'vermelha', 'ABC123')
carro_user = Carro('Fiat', 'Uno', 'azul', 'XYZ456')

print(moto_user.aumentar_acelerador())
print(moto_user.trocar_pneu())
print(moto_user.valida_ligada())
print(moto_user.valida_acelerador())

print("=="*20)

print(carro_user.ligar())
print(carro_user.abrir_capota())
print(carro_user.trocar_pneu())
print(carro_user.valida_ligada())
print(carro_user.valida_acelerador())