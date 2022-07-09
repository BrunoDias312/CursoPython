"""
Ler salario funcionario -> dar aumento de 25%
"""

salario_atual = float(input("Salario atual: "))

salario_pos = salario_atual + (salario_atual * 0.25)

print(f"Novo salario é de R${salario_pos:,.2f}")