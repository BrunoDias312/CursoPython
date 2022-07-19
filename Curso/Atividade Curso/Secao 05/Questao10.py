"""
Calcular altura e mostrar o peso
pegar sexo e altura
"""

#Entrada do user
sexo = input("Sexo(H/M): ")
altura = float(input("Altura em cm: "))

#Converter para metros
altura = altura / 100

#Verificar sexo - Saida de dados
if sexo == 'H' or sexo == 'h':
    print(f"Peso ideal de um homem, cuja altura é {altura:,.2f}.")
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal é {peso_ideal:,.2f};")
elif sexo == 'M' or sexo == 'm':
    print(f"Peso ideal de uma mulher, cuja altura é {altura:,.2f}.")
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal é {peso_ideal:,.2f};")
else:
    print("Entrada invalida!!!!")
