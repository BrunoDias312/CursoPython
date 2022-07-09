"""
Ler 4 notas - calcular media
"""

nota1 = float(input("Nota do Pedro: "))
nota2 = float(input("Nota da ana: "))
nota3 = float(input("Nota do Rafael: "))
nota4 = float(input("Nota do Andre "))

media_nota = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média dos alunos é {media_nota:,.2f}.")