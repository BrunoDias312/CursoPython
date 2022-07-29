"""
imprimir numeros impares ate o valor que o user digitou
"""
# Entrada do User
inicio = int(input("Valor: "))

for i in range(inicio+1):
    if i % 2 != 0:
        print(i)