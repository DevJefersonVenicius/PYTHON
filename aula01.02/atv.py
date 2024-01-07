# atv valendo 5 pontos
# Faça um sistema de controle de estoque que atenda as seguintas regras:
# 1. cadastro de produtos
# 2. controle de validade
# 3. controle de quantidade

import datetime

from datetime import datetime

class ControleEstoque:
    def __init__(self, nome, categoria, data_fabricacao, unidade):
        self.nome = nome
        self.categoria = categoria
        self.data_fabricacao = data_fabricacao
        self.unidade = unidade
        self.data_validade = 0
        self.retirar = 0
    
    def get_nome(self):
        return self.nome
    
    def get_categoria(self):
        return self.categoria
    
    def get_data_fabricacao(self):
        return self.data_fabricacao
    
    def get_unidade(self):
        return self.unidade
    
    def set_nome(self, nome_produto):
        self.nome = nome_produto
    
    def set_categoria(self, categoria_produto):
        self.categoria = categoria_produto

    def set_data_fabricacao(self, data_fabricacao_produto):
        self.data_fabricacao = data_fabricacao_produto

    def set_unidade(self, unidade_produto):
        self.unidade = unidade_produto
    
    def controle_de_validade(self):
        self.data_validade = '05/06/2024'
        data_dia = '01/02/2024'
        dv_coverter = datetime.strptime(self.data_validade, '%m/%d/%Y')
        dd_converter = datetime.strptime(data_dia, '%m/%d/%Y')
        qtd_dias = abs((dd_converter - dv_coverter).days)
        print(f'O produto vence em {qtd_dias} dias')
    
    def __str__(self):
        return f'Nome: {self.nome}; Categoria: {self.categoria}; Data de Fabricação: {self.data_fabricacao}; Unidades em estoque: {self.unidade - self.retirar}.'
        
    def controle_de_quantidade(self):
        self.retirar = int(input('Insira a quantidade que deseja retirar do estoque: '))
        estoque = self.unidade - self.retirar
        print(f'Restaram {estoque} unidades no estoque.')

  


refrigerante = ControleEstoque('Coca-Cola', 'Bebidas', '02/01/2024', 10)
print(refrigerante)
refrigerante.controle_de_validade()
print(refrigerante)
refrigerante.controle_de_quantidade()
print(refrigerante)
print(refrigerante)