"""
Ler determinados numeros inteiros e determinar se é par ou impar - terminar quando digitado 1000(mil)
"""

v_determinar = 1
while True:

    valor = int(input(f"Valor({v_determinar}): "))
    v_determinar+=1

    if valor != 1000:
        if valor % 2 == 0:
            print(f"valor {valor} é par.")


        else:
            print(f"valor {valor} é impar.")

    else:
        break


