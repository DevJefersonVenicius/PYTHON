class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Estudante(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

class EstudanteGraduacao(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

class EstudantePos(Pessoa):
    def __init__(self, nome, orientador, nivel):
        super().__init__(nome)
        self.orientador = orientador
        self.nivel = nivel
           
aluno = Estudante('Jeferson', 12345)
print(f'Olá {aluno.nome}, sua matricula é {aluno.matricula}.')
aluno2 = EstudanteGraduacao('Jeferson', 'Back-End')
print(f'Olá {aluno2.nome}, seu curso é {aluno2.curso}.')
aluno3 = EstudantePos('Jeferson', 'Paulo Junior', 4)
print(f'Olá {aluno3.nome}, seu nivel é {aluno3.nivel} e seu orientador é {aluno3.orientador}.')
