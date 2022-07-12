"""
Encontrar a distancia de X e Y de pontos R2 e calcule a sua origem (0,0)
"""

x = int(input(f"Informe X = "))

y = int(input(f"Informe Y = "))

distancia = int((((0 - x) ** 2) + ((0 - y) ** 2)) ** (1 / 2))

print(f"Distância da origem = {distancia}")