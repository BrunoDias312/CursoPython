"""
Fahrenheit -> Celsius

FORMULA
C = 5.0 * (F-32.0) + 9.0
F -> Temperatura em Fahrenheit
C -> Temperatura em Celsius
"""

# Entrada de dados
F = float(input("Temperatura em em Fahrenheit: "))

# Processamento
C = 5.0 * (F-32.0) / 9.0

# Saida de dados
print(f"A temperatura °{F} Fahrenheit em Celsius é °{round(C,2)};")