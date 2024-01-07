"""
Questão 02

• Faça a abstração da superclasse Extintor de Incendio.

Obs: você deve fazer o str dela mostrando o nivel da carga do extintor

---------------------------
|    ExtintorDeIncendio   |
---------------------------

"""
class ExtintorDeIncendio:
    def __init__(self, nome):
        self.nome = nome
        self.carga = 0
        self.ligado = False

    def get_nome(self):
        return self.nome
    
    def get_carga(self):
        return self.carga
    
    def set_nome(self, meu_nome):
        self.nome = meu_nome

    def set_carga(self, nova_carga):
        if self.ligado == True and nova_carga >= 0 and nova_carga <= 100:
            self.carga = nova_carga
            print(f'Carga mudada para {self.carga}')
        
        elif self.ligado == True and nova_carga < 0 or nova_carga > 100:
            print('Carga adicionada inexistente')
        
        else:
            print('Carga não pode ser alterada, extintor está desligado')
    
    def ligar(self):
        self.ligado = True
        print('Extintor foi ligado')
    
    def desligar(self):
        self.ligado = False
        self.carga = 0
        print('Extintor foi desligado')
    
    def valida_ligada(self):
        if self.ligado == True:
            return 'ligado'
        else:
            return 'desligado'
           
    def __str__(self):
        return f'{self.nome}: está {self.valida_ligada()}. Sua carga atual é de: {self.carga}'

user = ExtintorDeIncendio('Extintor 2000')

user.ligar()
print(user)
user.desligar()
print(user)
user.set_carga(24)
print(user)
user.ligar()
print(user)
user.set_carga(90)
print(user)
user.desligar()
print(user)
user.set_carga(-98)
print(user)
user.ligar()
print(user)
user.set_carga(-98)
print(user)