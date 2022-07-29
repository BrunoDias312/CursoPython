"""
Fazer uma serie harmonica
"""

valor = int(input("Valor: "))
soma = 0

for i in range(1, valor+1):
    soma += 1 / i

print(soma)