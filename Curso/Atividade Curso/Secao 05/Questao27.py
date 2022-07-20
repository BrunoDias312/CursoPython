"""
Classificar o nadador de acordo com a idade
"""

idade_nadador = int(input("A idade do nadador: "))

if idade_nadador == 5 or idade_nadador <= 7:
    print("Infantil A")
elif idade_nadador == 8 or idade_nadador <= 10:
    print("Infantil B")
elif idade_nadador == 11 or idade_nadador <= 13:
    print("Juvenil A")
elif idade_nadador == 14 or idade_nadador <= 17:
    print("Juvenil B")
elif idade_nadador > 18:
    print("Sênior")