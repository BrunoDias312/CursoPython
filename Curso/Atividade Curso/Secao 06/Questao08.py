"""
Imprimir apenas o maior valor lido e o menor
"""

atual_maior = 0
atual_menor = 0
contador = 0

for i in range(3):
    valor = int(input(f"Valor({i+1}): ")) # Entrada do user
    contador+=1 #adicionar valor ao contador

    if contador == 1:# Adicionando valor ao atual_maior e atual_menor
        atual_maior = valor
        atual_menor = valor

    else:
        if valor >= atual_maior or valor <= atual_menor:# Verificação
            if valor >= atual_maior:
                atual_maior = valor

            if valor <= atual_menor:
                atual_menor = valor
                print(valor)

# Saida para o user
print(f"Valor maior digitado: {atual_maior}.")
print(f"Valor menor digitado: {atual_menor}.")
