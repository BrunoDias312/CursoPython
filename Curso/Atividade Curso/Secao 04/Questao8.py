"""
Kelvin -> Celsius

FORMULA
C = K - 273.15
C -> Celsius
K -> Kelvin
"""

# Entrada de dados
K = float(input("Temperatura em em Kelvin: "))

# Processamento
C = K - 273.15

# Saida de dados
print(f"A temperatura °{K} Kelvin em Celsius é °{round(C,2)};")