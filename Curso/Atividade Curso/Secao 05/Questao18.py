"""
Menu - 4 opções - basicas matematicas
"""
#Menu
print("<----- Menu ----->")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("___________________\n")

#Entrada do User
escolha = int(input("Entrada: "))

#Tragetoria de escolha
if escolha == 1:
    print("\nA sua escolha foi 'Soma'")
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))

    resultado = a + b

    print(f"{a} + {b} = {resultado}")

elif escolha == 2:
    print("\nA sua escolha foi 'Subtração'")
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))

    resultado = a - b

    print(f"{a} - {b} = {resultado}")

elif escolha == 3:
    print("\nA sua escolha foi 'Multiplicação'")
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))

    resultado = a * b

    print(f"{a} * {b} = {resultado}")

elif escolha == 1:
    print("\nA sua escolha foi 'Divisão'")
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))

    resultado = a / b

    print(f"{a} / {b} = {resultado}")

else:
    print("Entrada invalida")