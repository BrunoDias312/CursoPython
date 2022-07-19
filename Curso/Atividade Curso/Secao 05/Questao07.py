"""
Descobir se o numero qual numero é maior
"""

#Entrada de valores
numA = float(input("Digite o valor: "))
numB = float(input("Digite o segundo valor: "))

#verificado de tamanho - Saida de dados
if numA > numB:
    print("Primeiro valor digitado é maior que o segundo.")
elif numA < numB:
    print("Segundo valor é maior que o primeiro valor.")
elif numA == numB:
    print("Números iguais")
