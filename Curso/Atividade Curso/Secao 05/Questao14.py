"""
Calcular a media ponderada de 3 valores diciplinares
0 - 10 de notas
"""

#Entrada de notas e pesos
nota_trabalho_laboratorio = float(input("Nota do trabalho do laboratorio: "))
peso_trabalho_laboratorio = 2
print("--------------------------------------------------------------------->")

nota_avaliacao_semestral = float(input("Nota da avaliação semestral: "))
peso_avaliacao_semestral = 3
print("--------------------------------------------------------------------->")

exame_final = float(input("Nota do exame final: "))
peso_exame_final = 5
print("--------------------------------------------------------------------->")

#Calculo das notas
total_mult = nota_trabalho_laboratorio * peso_trabalho_laboratorio + nota_avaliacao_semestral * peso_avaliacao_semestral + exame_final * peso_exame_final
total_soma = peso_exame_final + peso_avaliacao_semestral + peso_trabalho_laboratorio
media = total_mult / total_soma

if 0 <= media <= 2.9:
    print("Aluno Reprovado!!!")
    print(f"Nota do aluno é {media:,.2f}.")
elif 3 <= media <= 4.9:
    print("Aluno em recuperação!!!")
    print(f"Nota do aluno é {media:,.2f}.")
elif media >= 5 and media <= 10:
    print("Aluno Aprovado!!!")
    print(f"Nota do aluno é {media:,.2f}.")
else:
    print("Notas digitadas são invalidas!!!")
