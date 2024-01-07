"""
Questão 03

• Faça a abstração de superclasse Fabrica de Rações. 

Obs: você deve ter um str mostrando cada status da fabrica

-------------------------
|    FabricaDeRacoes    |
-------------------------

"""
class FabricaDeRacoes:
    def __init__(self, nome):
        self.nome = nome
        self.preco_kg = 0
        self.total_compra_kg = 0
        self.nome_racao = 'Gato' and 'Cachorro'

    def get_nome(self):
        return self.nome

    def get_preco_kg(self):
        return self.preco_kg

    def set_nome(self, meu_nome):
        self.nome = meu_nome

    def set_preco_kg(self, novo_preco):
        self.preco_kg = novo_preco

    def compras(self):
        self.total_compra_kg = int(input('Quantos kilos você quer comprar: '))
        return self.total_compra_kg

    def vendas(self):
        return self.total_compra_kg * self.preco_kg

    def racao(self):
        while self.nome_racao:
            print(f'BEM VINDO A FABRICA DE RAÇÕES {self.nome}')
            self.nome_racao = input('Digite a ração que você quer comprar: Digite: "Gato" ou "Cachorro": ').lower()
            
            if self.nome_racao == 'gato':
                self.preco_kg = 4
                break
            
            elif self.nome_racao == 'cachorro':
                self.preco_kg = 5
                break
            
            else:
                print('Você digitou de forma errada, digite a ração novamente!')

    def __str__(self):
        return f'Você comprou {self.compras()}kg de ração de {self.nome_racao} e pagou {self.vendas()}R$'

comprador = FabricaDeRacoes('ANIMAIS FELIZES!!!')
comprador.racao()
print(comprador)