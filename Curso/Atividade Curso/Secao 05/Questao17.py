"""
Calcular a area de um trapézio
"""

#entrada das bases e da altura do trapezio
base_maior = float(input("Base maior: "))
base_menor = float(input("Base menor: "))
altura = float(input("Altura: "))

if base_maior > 0 and base_menor > 0:
    #Calcular o Trapezio
    area = ((base_maior + base_menor) * altura) / 2

    #Saida do resultadod
    print(f"A area do Trapézio é de {area:,.2f}cm.")

else:
    print("As bases sao menores que 0")
