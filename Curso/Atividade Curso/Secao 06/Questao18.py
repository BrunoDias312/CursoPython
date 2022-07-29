"""
ler maior numero digitado e quantas vezes foi digitado o maior numero
"""

# Declaração de variaveis
index = 0
qtd_maior = 0
contador = 0

qtd = int(input("Quantidade de repetições: "))# Entrada do user

while index <= qtd-1:
    valor = int(input(f"Valor({index + 1}): "))  # Entrada do user
    contador += 1  # adicionar valor ao contador

    if contador == 1:  # Adicionando valor ao atual_maior e atual_menor
        atual_maior = valor
        atual_menor = valor
        qtd_maior+=1

    else:
        # Verificação
        if valor >= atual_maior:
            atual_maior = valor
            qtd_maior += 1
    index+=1

# Saida para o user
print(f"Valor maior digitado: {atual_maior} e foi digitado o maior valor {qtd_maior}x.")
