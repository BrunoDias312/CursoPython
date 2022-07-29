"""
Ler 10 valores e imprimir a sua media
"""

qtd = 0
soma = 0
media = 0

while qtd <= (10-1):
    valor = int(input(f"Valor({qtd+1}): "))
    soma = soma + valor
    qtd = qtd+1

media = soma / qtd
print(f"A media dos numeros é {media}")