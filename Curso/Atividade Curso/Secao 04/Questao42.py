"""
Salario base - Calcular
"""

# Entrada de dados
salario_base = float(input("Salario Base: "))

gratificacao = 0.05 * salario_base #60
gratificacao = 0
imposto = 0.28 * salario_base #84

salario_receber = salario_base + gratificacao - imposto

print("Irantificação: ", gratificacao)
print("Imposto: ", imposto)
print("Salario do funcionario: R$", salario_receber)