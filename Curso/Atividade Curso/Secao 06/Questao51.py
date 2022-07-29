"""
Calcular o salario de um funcionario -
    aumento anual de 1,5% - cada ano corresponde ao dobro do ano anterior
"""

# Declaração de variaveis
salario = 2000
taxa_juros = 0.015
taxa_juros_atual = 0
ano_atual = 2022
aumento = 30

# Inicio Real
for ano in range(1996, ano_atual + 1, 1):
    # salario = (salario * taxa_juros) + salario
    salario = (salario + aumento)
    aumento = 30 * 2

    # taxa_juros_atual = (taxa_juros * 2)
    # taxa_juros = taxa_juros_atual

    print(f"Ano {ano} - Salario R${salario:,.2f}")
