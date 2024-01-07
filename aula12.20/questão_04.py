"""
Questão 04

• Faça a abstração de superclasse Bichinho Virtual. Você deve ter os atributos: nome, energia, brincar e dormir

Regras: ao brincar o bichinho gasta energia e se a energia atingir um nivel imposto por você ele deve dormir para recarregar.

Obs: você deve ter um str mostrando o status completo do seu bichinho virtual

-------------------------
|    BichinhoVirtual    |
-------------------------

"""
class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.brincar = 0
        self.vivo = True

    def get_nome(self):
        return self.nome

    def set_nome(self, meu_nome):
        self.nome = meu_nome

    def get_energia(self):
        return self.energia

    def set_energia(self, nova_energia):
        self.energia = nova_energia

    def get_brincar(self):
        return self.brincar

    def set_brincar(self, nova_brincar):
        while self.vivo:
            print(f'Brinque com o(a) {self.nome}!!!')
            nova_brincadeira = int(input('Digite o total de brincadeiras para fazer com seu Pet (máximo 90): '))
            
            if nova_brincadeira < 0 or nova_brincadeira > 100:
                print('Brincadeira inválida. Digite um valor entre 0 e 100.')
                continue

            nova_brincadeira = min(nova_brincadeira, 90)
            self.brincar += nova_brincadeira
            energia_gasta = nova_brincadeira
            self.energia -= energia_gasta

            if self.energia <= 0:
                print(f'Oh não! {self.nome} ficou sem energia e morreu. Fim de jogo.')
                self.vivo = False
            elif self.brincar >= 90:
                resposta_dormir = input('Seu Pet está cansado. Deseja deixar seu Pet dormir? (s/n): ')
                if resposta_dormir.lower() == 's' and 'n':
                    self.dormir()
                    break
                else:
                    print('Continue brincando com seu Pet!')
            else:
                print(f'Seu Pet ainda tem energia ({self.energia})! Brinque mais com seu Pet!!!')

    def dormir(self):
        print(f'{self.nome} está dormindo para recarregar energia...')
        self.energia = 100
        self.brincar = 0

    def imprimir(self):
        print(f'Olá me chamo {self.nome}.')
        print(f'Minha energia está em {self.energia}.')
        print(f'Meu nível de brincadeira está em {self.brincar}.')

meu_pet = BichinhoVirtual('Leãozinho')
meu_pet.imprimir()
meu_pet.set_brincar(0)
meu_pet.imprimir()
