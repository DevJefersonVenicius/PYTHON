class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, CPF: {self.get_cpf()}'

class Aluno(Pessoa):
    def __init__(self, nome, idade, cursa,):
        self.cursa = cursa
        super().__init__(nome, idade)
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, CPF: {self.get_cpf()}'

paulo = Professor('Paulo Junior', 29, 1400.00, 'Back-End')
paulo.set_cpf(1234567890)
print(paulo)
jeferson = Aluno('Jeferson Venicius', 19, 'Back-End')
jeferson.set_cpf(9876543210)
print(jeferson)