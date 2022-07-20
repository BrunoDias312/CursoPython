"""
Mostrar na tela a equação selecionada para o user
"""

#Tipo de operação
import math

opcao = input("Geométrica - Ponderada - Harmôica - Aritmética:\n")

#entrada das medidas
x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))

if opcao.lower() == 'geometrica':
    print(f"{math.sqrt(x*y*z):,.2f}")
elif opcao.lower() == 'ponderada':
    print(f"{(x + 2 * y + 3 * z) / 6:,.2f}")
elif opcao.lower() == 'harmonica':
    print(f"{1 / (1/x + y/3 + 1/z):,.2f}")
elif opcao.lower() == 'aritmetica':
    print(f"{(x+y+z)/3}")
else:
    print("Opcão invalida")
