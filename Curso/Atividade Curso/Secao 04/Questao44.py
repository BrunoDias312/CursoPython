"""
    Altura do degrau - Altura que o user deseja subir e calcular ate onde iria o user
"""

altura_degrau = float(input("Altura do degrau: ")) # CM
altura_alcancar = float(input("Altura a alcancar: "))# Metros

altura_degraMetros = altura_degrau / 100

altura_subir = altura_alcancar / altura_degraMetros

print("quantidade de degraus que precisar subir é de",altura_subir, ".")