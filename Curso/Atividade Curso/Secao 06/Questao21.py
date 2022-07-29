"""
Receber 2 valores - mostrar soma dos pares e a multiplicação dos impares - dentro dos valores
"""

#Declaração das variaveis
soma = 0
multiplicacao = 1

# Entrada do user
valor_inicial = int(input("Valor inicial: "))
valor_final = int(input("Valor final: "))

for i in range(valor_inicial, valor_final):
    if i % 2 == 0: # Se par
        soma = soma + i

    if i % 2 != 0:
        multiplicacao = multiplicacao * i

#Saida para o user
print(f"Soma dos pares é {soma}.")
print(f"Multiplicação dos impares é {multiplicacao}.")
