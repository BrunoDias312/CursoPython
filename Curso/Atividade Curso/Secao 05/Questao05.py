"""
Verificar se o numero é par ou impar
"""

#entrada do user
num = int(input("Digite um numero: "))

verificador = num%2
if verificador == 0:
    print("Numero é par.")
else:
    print("Numero é impar.")