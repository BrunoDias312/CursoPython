"""
Calcular uma sequencia de numeros
"""
# Declaração de variaveis
soma1 = 0
soma2 = 0
soma3 = 0

valor = int(input("Valor: "))# Entrada do user

for i in range(valor+1):
    soma1 += 1

    if i % 2 == 0:
        soma2-= i

    if i % 2 != 0:
        soma3 += i
        print(soma3)

# Saida de usuario
print(f"1° sequencia: {soma1}")
print(f"2° sequencia: {soma2}")
print(f"3° sequencia: {soma3}")

