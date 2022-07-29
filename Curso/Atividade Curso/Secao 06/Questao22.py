"""
Validas notas de 10 a 20 e mostrar na tela a correspodente media aritmética
    Programa termina quando colocado um valor invalido
"""

corresp = 1
media = 0
div = 0
nota = 0
while True:
    valor = int(input(f"Nota({corresp}): "))
    corresp+=1

    if valor < 10 or valor > 20:# Força saida do loop
        break

    div+=1# Para fazer a media
    nota = nota + valor
    media = nota / div
print(media)
