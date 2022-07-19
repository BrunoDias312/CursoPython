"""
verificar se o numero é positivo, e calcular se for
"""
import math

#Entrada de user
num = float(input("Digite um valor: "))

#Verificação de numero - se é maior que 0
if num > 0:
    #Calcular
    raiz = math.sqrt(num)
    num2 = num**2

    #Saida de dados
    print(f"A raiz de {num:,.2f} é {raiz:,.2f}, e ele ao quadrado é {num2:,.2f}.")

else:
    print("O numero digitado é negativo.")