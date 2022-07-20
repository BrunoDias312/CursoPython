"""
Descobrir atravez de A, B, C de qual triangulo se encaixa
"""

#Entrada dos lados
a = int(input("Entrada do lado A: "))
b = int(input("Entrada do lado B: "))
c = int(input("Entrada do lado C: "))

if a == b and a == c and b == c:
    print("Triangulo Equilatero.")
elif a == b or b == c:
    print("Triangulo isóceles.")
elif a != b and a != c and b != c:
    print("Triangulo Escaleno.")
