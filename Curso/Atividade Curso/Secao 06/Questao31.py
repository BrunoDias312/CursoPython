"""
Calcular  o valor de S
"""

divisao = 0
soma = 0

for index in range(1, 100):
    for i in range(1, 51, 2):
        divisao = index / i
        soma = soma + divisao
        print(f"{index}/{i}")

print(f"{soma:,.2f}")