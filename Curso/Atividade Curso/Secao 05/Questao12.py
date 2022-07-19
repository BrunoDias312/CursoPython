"""
Calcular o logaritimo de um numero, se positivo
"""
import math

num = int(input("Digite um numero: "))

if num > 0:
    print(f"o log de Log{num} é {math.log(num):,.2f}")