"""
Simular 2 valores, 'n' vezes e verificar se eles são (<,>,=)
"""

qtd = 0

n = int(input("Numero de repetição: "))

while qtd <= n-1:
    qtd+=1
    d1 = int(input(f"Valor({qtd})"))
    d2 = int(input(f"Valor({qtd})"))

    if d1 > d2:
        print("D1 > D2")
    elif d1 < d2:
        print("D1 < D2")
    else:
        print("D1 = D2")
