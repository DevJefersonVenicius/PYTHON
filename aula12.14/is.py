# nome = 'JefersonVenicius'
# print(nome.isalpha()) # Retorna True caso todas as strings da variavel sejam de A a Z, não pode conter espaçõs

# nome2 = '0123456789'
# print(nome2.isdigit()) # Retorna True caso todas as strings da variavel sejam números, não pode conter espaçõs

# nome3 = '0293847' # Retorna True caso todas as strings da variavel sejam números, não pode conter espaçõs
# print(nome3.isdecimal())

class Pet:

    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.sede = 0
        self.comida = 100
    
    # GETS
    def get_nome(self):
        return self.nome
    
    def get_peso(self):
        return self.peso
    
    def get_fome(self):
        return self.fome
    
    def get_sede(self):
        return self.sede

    # SETS
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def set_fome(self, nova_fome):
        self.fome += nova_fome
        while self.fome >= 99:
            diferenca = self.fome - 99
            print(diferenca)
            print(f'Alimente o(a) {self.nome}!!!')
            nova_comida = int(input('Quanto de comida você quer dar para seu Pet? '))
            self.fome -= nova_comida
                
    def set_sede(self, nova_sede):
        self.sede = nova_sede
    
    def imprimir(self):
        print(f'Olá me chamo {self.nome}.')
        print(f'Estou pesando {self.peso}Kg.')
        print(f'Minha fome está em {self.fome}.')
        print(f'Minha sede está em {self.sede}.')
        
caozinho = Pet('Bodo', 15)
caozinho.imprimir()
caozinho.set_fome(20)
caozinho.imprimir()
caozinho.imprimir()
caozinho.set_fome(30)
caozinho.imprimir()
caozinho.set_fome(70)
caozinho.imprimir()
caozinho.set_fome(10)
caozinho.imprimir()





    


