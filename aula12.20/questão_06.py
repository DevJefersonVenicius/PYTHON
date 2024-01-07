"""
Questão 06 - BÔNUS

• Faça a abstração de superclasse Livros.

Obs: você deve ter os atributos codigo, nome, qtdPaginas, autor e preço. Todos utilizando o metodo de property
Obs: Você deve fazer um metodo de venda do livro. Onde simulo o pagamento e finalizo a compra.
Obs: você deve ter um str

----------------
|    Livros    |
----------------

"""
class Livros:
    def __init__(self):
        self.__nome = None
        self.__qtdpaginas = None
        self.__autor = None
        self.__preco = None
        self.quantidade_comprada = None

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, meu_nome):
        self.__nome = meu_nome

    def get_qtdpaginas(self):
        return self.__qtdpaginas
    
    def set_qtdpaginas(self, minhas_paginas):
        self.__qtdpaginas = minhas_paginas

    def get_autor(self):
        return self.__autor
    
    def set_autor(self, meu_autor):
        self.__autor = meu_autor
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, meu_preco):
        self.__preco = meu_preco

    nome = property(get_nome, set_nome)
    qtdpaginas = property(get_qtdpaginas, set_qtdpaginas)
    autor = property(get_autor, set_autor)
    preco = property(get_preco, set_preco)
    
    def comprar(self):
        print('Bem vindo à livraria Boa Vida.')
        print(f'O livro disponível para venda hoje é: {self.get_nome()}.')
        self.quantidade_comprada = int(input('Digite quantas unidades do livro você quer comprar: '))
        print(f'Compra finalizada para {self.quantidade_comprada} unidades de {self.get_nome()}.')

    def __str__(self):
        total_pago = self.quantidade_comprada * self.get_preco()
        return f'Livro: {self.get_nome()}. Autor: {self.get_autor()}. Quantidade de Páginas: {self.get_qtdpaginas()}. Preço: R${self.get_preco():.2f}. Você pagou R${total_pago:.2f} em {self.quantidade_comprada} livros.'

livro = Livros()
livro.set_nome('Os Três Porquinhos')
livro.set_autor('José Albino')
livro.set_qtdpaginas(200)
livro.set_preco(100)
livro.comprar()
print(livro)