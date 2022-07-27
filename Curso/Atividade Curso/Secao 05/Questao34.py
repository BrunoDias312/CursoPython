"""
Ler notas e faltas de um aluno - escreva seu conceito
"""

#Entrada do user
nota_aluno = float(input("Nota Aluno: "))
qtd_faltas = int(input("Faltas do aluno: "))

#Conceitos
if 9 <= nota_aluno <= 10:# Nota
    if qtd_faltas <= 20:# Faltas
        print("Conceito A")
    else:
        print("Conceito B")

elif 7.5 <= nota_aluno <= 8.9:# Nota
    if qtd_faltas <= 20:# Faltas
        print("Conceito B")
    else:
        print("Conceito C")

elif 5 <= nota_aluno <= 7.4:# Nota
    if qtd_faltas <= 20:# Faltas
        print("Conceito C")
    else:
        print("Conceito D")

elif 4 <= nota_aluno <= 4.9:# Nota
    if qtd_faltas <= 20:# Faltas
        print("Conceito D")
    else:
        print("Conceito E")

elif 0 <= nota_aluno <= 3.9:# Nota
    if qtd_faltas <= 20:# Faltas
        print("Conceito E")
    else:
        print("Conceito E")