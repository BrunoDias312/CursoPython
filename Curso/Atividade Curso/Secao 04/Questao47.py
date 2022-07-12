"""
Leia um numero e digite um numeoro por linha - maior que 1000 e menor que 9999
"""

numero = int(input("Entrada do numero: "))

if 1000 <= numero <= 9999:
    num = str(numero)
    print(num[0])
    print(num[1])
    print(num[2])
    print(num[3])
else:
    print("Fora de contexto... Tente novamente!!!")