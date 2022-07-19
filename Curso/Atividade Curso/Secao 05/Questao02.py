"""
Encontrar a raiz quadrada
"""
import math
#Entrada de user
num = int(input("Entrada de valor: "))

#Verificação de numero
if num >= 0:
    num = math.sqrt(num)
    print(num)
else:
    print("O numero digitado é invalido")