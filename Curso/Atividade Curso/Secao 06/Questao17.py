"""
Calcular a soma ate 'n', que o user digitou
"""

valor = int(input("Valor: "))
soma = 0

for i in range(0, (valor+1), 1):
    soma = soma + i
print(soma)