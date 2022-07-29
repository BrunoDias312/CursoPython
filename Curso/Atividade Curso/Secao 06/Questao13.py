"""
imprimir numeros pares ate o valor que o user digitou
"""

valor = int(input("Valor: "))# Entrada do User

for i in range(valor+1):
    if i % 2 == 0:
        print(i)
