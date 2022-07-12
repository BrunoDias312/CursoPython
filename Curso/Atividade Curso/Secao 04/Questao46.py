"""
inverter a possicao de numeros de apenas 3 digitos
"""

entrada = int(input("Entrada do numero: "))

if 100 <= entrada <= 999:
    numero_invertido = int(str(entrada)[::-1])
    print(f"Numero invertido: {numero_invertido}.")
else:
    print("Fora de contexto... Tente novamente!!!")