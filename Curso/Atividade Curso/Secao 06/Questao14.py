"""
imprimir numeros pares ate o valor que o user digitou, em ordem decrecente
"""

# Entrada do User
inicio = int(input("Valor: "))

for i in range(inicio, (0-1), -1):
    if i % 2 == 0:
        print(i)