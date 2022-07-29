"""
Imprimir numeros em ordem decrescente de 0 até a entrada do user
"""

inicio = int(input("Valor final(vai em ordem decrescente):"))

for i in range(inicio, (0-1), -1):
    print(i)
