class Televisao:
    def __init__(self, tamanho): 
        self.tamanho = tamanho
        self.canal = 0
        self.ligada = False
    
    # GETS
    
    def get_tamanho(self):
        return self.tamanho
    
    def get_canal(self):
        return self.canal
    
    # SETS

    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
    
    def set_canal(self, novo_canal):
        if self.ligada == True and novo_canal >= 0 and novo_canal <= 999:
            self.canal = novo_canal
            print(f'Canal mudado para o {self.canal}')
        
        elif novo_canal < 0 or novo_canal > 999:
            print('Canal inexsistente')
        
        else:
            print('Favor ligar a TV para mudar o canal')
        
    # METODOS

    def ligar(self):
        self.ligada = True
        print('Sua TV está ligada')
    
    def desligar(self):
        self.ligada = False
        print('Sua TV está desligada')

    def valida_ligada(self):
        if self.ligada == True:
            return 'ligada'
        else:
            return 'desligada'
    
    def __str__(self):
        return f'Sua TV está {self.valida_ligada()} o canal atual é o {self.canal} e o tamanho dela é {self.tamanho}'
    
    def mudar_canal(self):
        self.canal = self.ligar

# CHAMADAS DE CRIAÇÃO
minha_tv = Televisao(32)
minha_tv.ligar()
minha_tv.desligar()
minha_tv.set_canal(10)
print(minha_tv.get_canal())
minha_tv.ligar()
minha_tv.set_canal(100)
print(minha_tv.get_canal())
print(minha_tv)
minha_tv.desligar()
print(minha_tv)