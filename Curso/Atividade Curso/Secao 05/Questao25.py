"""
Calcular delta e baskra
"""
import math

print("Calcular equação de 2° grau.")
#entrada do user
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print("<---------------------------------->")

#Mostar na tela a formula
print("\nFormula da equacão de 2° grau: ")
print("ax² + bx + c = 0")
print(f"{a}² + {b} + {c} = 0")
print("\nFormula de delta: ")
print(f"Delta = b² - 4 * a * c")
print(f"Delta = {b}² - 4 * {a} * {c}\n")
print("<---------------------------------->")

delta = (b**2) - 4 * a * c # Calculando delta

print(f"Delta: {delta}")

if delta < 0:
    print("Não existe raiz")

elif delta == 0:
    print("Raiz única")

elif delta > 0:
    x1 = (b**2 + math.sqrt(delta)) / (2 * a)
    x2 = (b**2 - math.sqrt(delta)) / (2 * a)
    print(f"X¹: {x1}\nX²: {x2}")
