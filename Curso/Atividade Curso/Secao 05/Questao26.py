"""
Calcular km/l consumidos por um carro em um determinado percuso
"""

#Entrada de valores
km = float(input("Distancia em KM: "))
litros = float(input("Litros consumidos: "))

#calculo para descobrir
consumido = km // litros
#km_rodado = consumido * litros

if consumido < 8:
    print("Venda o carro!")
elif 8 <= consumido <= 14:
    print("Economico!")
elif consumido > 12:
    print("Super economico!")