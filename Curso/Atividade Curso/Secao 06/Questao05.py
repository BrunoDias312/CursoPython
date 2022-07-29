"""
Digitar 10x e entao somar os valores
"""

# Declaração de variaveis
qtd = 0
soma = 0

# Inicio de Loop
while qtd <= (10-1):
    valor = int(input(f"Digite o valor({qtd+1}): "))
    soma = soma + valor
    qtd = qtd + 1

# Saida para o user
print(f"Soma dos valores: {soma}")