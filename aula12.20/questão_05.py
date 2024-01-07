"""
Questão 05

• Faça a abstração de superclasse Formas Geométricas.

Obs: você deve fazer o cálculo da área e do perímetro das formas
Obs: você deve fazer quantos str forem necessarios para sua abstração

----------------------------
|    FormasGeometricas    |
----------------------------

"""
class FormasGeometricas:
    def __init__(self, calculadora):
        self.calculadora = calculadora
        self.area_quadrado = None
        self.perimetro_quadrado = None
        self.base = 0
        self.altura = 0
        self.tamanho_lados = 0
    
    def calcular_area_quadrado(self):
        self.base = float(input('Digite a area do quadrado: '))
        self.altura = float(input('Digite a altura do quadrado: '))
        self.area_quadrado = self.base * self.altura
        return self.area_quadrado

    def calcular_perimetro_quadrado(self):
        self.tamanho_lados = float(input('Digite o tamanho dos lados: '))
        self.perimetro_quadrado = 4 * self.tamanho_lados
        return self.perimetro_quadrado
    
    def __str__(self):
        return f'Area: {self.area_quadrado}; Perimetro: {self.perimetro_quadrado}'
    
calculo = FormasGeometricas('Calculadora 2000')
calculo.calcular_area_quadrado()
calculo.calcular_perimetro_quadrado()
print(calculo)