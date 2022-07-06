"""
Km/h -> M/s

FORMULA
M = K / 3.6
K -> Velocidade em km/h
M -> Velocidade em m/s
"""

# Entrada de dados
K = int(input("Velocidade em KM/h: "))

# Processamento

M = K / 3.6# Conforme o valor digitado em K a variavel sera M será float

# Saida de dados
print(f"{K}KM/h em {round(M,2)}M/s;")
