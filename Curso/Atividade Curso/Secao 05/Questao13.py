"""
Media ponderada de notas de 3 alunos
"""

#Entrada de notas e pesos
nota1 = float(input("Nota do aluno: "))
peso1 = float(input("Peso da nota: "))
print("------------------------------")

nota2 = float(input("Nota do aluno: "))
peso2 = float(input("Peso da nota: "))
print("------------------------------")

nota3 = float(input("Nota do aluno: "))
peso3 = float(input("Peso da nota: "))
print("------------------------------\n")

total_mult = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
total_soma = peso1 + peso2 + peso3
total_total = total_mult / total_soma

if total_total >= 60:
    print("Aluno Aprovado!!!")
    print(f"O total de nota media foi de {total_total:,.2f}.")
elif total_total < 60:
    print("Aluno Reprovado!!")
    print(f"O total de nota media foi de {total_total:,.2f}.")
