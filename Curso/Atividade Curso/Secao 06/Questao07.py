"""
Calcular 10 numeros inteiros possitivos, apenas positivos, ignorando os negativos e entao calcular sua media
"""

# Declaração de variaveis
qtd = 0
soma = 0
media = 0

# Loop
while qtd <= (10-1):
    valor = int(input(f"Valor({qtd+1}): "))
    if valor < 0:
        qtd = qtd + 1
        continue
    else:
        soma = soma + valor
        qtd = qtd + 1

media = soma / qtd

#Saida user
print(f"A media dos {qtd} valores é {media} .")