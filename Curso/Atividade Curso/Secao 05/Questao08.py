"""
Notas de alunos - se validas imprimir a media
senao terminar o programa
"""

#Entrada de notas pelo user
nota1 = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a segunda nota: "))

if 0 < nota1 <= 10 and 0 < nota2 <= 10:
    media = (nota1 + nota2) / 2
    print(f"A média é {media:,.2f}.")
else:
    print("Nota invalida.")
    exit()