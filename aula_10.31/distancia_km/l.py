km = float(input('Digite a distancia: '))
l = float(input('Digite os litros de combustivel: '))
consumo = km / l

if consumo < 8:
    print('O consumo é menor que 8 "VENDA O CARRO": ', consumo)

if consumo == 8 and 14:
    print('O consumo é Económico entre 8 e 14 "ECONÓMICO": ', consumo)

if consumo > 14:
    print('O consumo é maior que 14 "SUPER ECONÓMICO": ', consumo)