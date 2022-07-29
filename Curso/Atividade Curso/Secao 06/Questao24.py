"""
Descobrir quais os numeros e divisor ate chegar ao numero que o user digitou e por ultimo somar
"""

valor = int(input("Valor: "))
soma = 0

for i in range(1, valor+1):
    if valor % i == 0:
        soma = soma + i
        print(i, end=" ")

print("a soma é", soma - valor)