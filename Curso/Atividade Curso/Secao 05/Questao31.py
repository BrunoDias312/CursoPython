"""
Classificar por peso e altura de acordo com a tabela
"""

#Entrada do user
altura = float(input("Entrada de altura: "))
peso = float(input("Entrada de altura: "))

#Classificação
if altura <= 120: #Classificar pessoas menores que 120cm
    if peso <= 60:
        print("Classificação A")
    elif 61 <= peso <= 90:
        print("Classificação D")
    elif peso > 90:
        print("Classificação G")

elif 121 <= altura <= 170:#Classificar pessoas menores que 170cm
    if peso <= 60:
        print("Classificação B")
    elif 61 <= peso <= 90:
        print("Classificação E")
    elif peso > 90:
        print("Classificação H")

elif altura > 170:#Classificar pessoas maiores que 170
    if peso <= 60:
        print("Classificação C")
    elif 61 <= peso <= 90:
        print("Classificação F")
    elif peso > 90:
        print("Classificação I")