"""
Mostrar qual numero é maior e a diferença entre os numeros
"""

#Entrada do user
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    diferenca = num1 - num2
    print(f"{num1} é maior que {num2} e a diferenca dos valores é de {diferenca}.")

if num1 < num2:
    diferenca = num2 - num1
    print(f"{num2} é maior que {num1} e a diferenca dos valores é de {diferenca}.")