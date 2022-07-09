"""
Calcular a hipotenusa
"""
import math
a = float(input("Valor de A: "))
b = float(input("Valor de B: "))

hipotenusa = math.sqrt((a**2)+(b**2))

print(round(hipotenusa, 2))