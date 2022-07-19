"""
imprimir a raiz se positivo, caso contrario o numero ao quadrado
"""
import math

#entrada
num = float(input("Ditite um numero: "))

if num > 0:
    raiz = math.sqrt(num)
    print(f"{raiz:,.2f}")
else:
    num2 = num **2
    print(f"{num2:,.2f}")
