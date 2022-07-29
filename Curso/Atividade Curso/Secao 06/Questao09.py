"""
ler um int e entao imprimir  os numeros n impares
"""

i = 0
v = 0
qtd = int(input("Quantidade de impares: "))

while i <= qtd:
    valor = i % 2

    if valor != 0: # Se impar
        print(f"O {i}° numero impar é {i}")
        i += 1
        v += 1

    else:
        i+=1
        v+=1
