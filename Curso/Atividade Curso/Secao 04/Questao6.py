"""
Celsius -> Fahrenheit

FORMULA
F = C * (9.0/5.0) + 32
F -> Temperatura em Fahrenheit
C -> Temperatura em Celsius
"""
# Entrada de dados
C = float(input("Temperatura em em Celsius: "))

# Processamento
F = C * (9.0/5.0) + 32.0

# Saida de dados
print(f"A temperatura °{C} Celcius em Fahrenheit é °{round(F,2)};")