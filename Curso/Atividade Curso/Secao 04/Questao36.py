"""
Encontrar o volume do cilindro
"""
pi = 3.141592

# Entrada de dados
altura = float(input("Entrada da altura: "))
raio = float(input(("Entrada do raio: ")))

# Processamento
volume = pi * raio**2 *altura

print(f"O volume do cilindro é de {volume:,.2f}")
