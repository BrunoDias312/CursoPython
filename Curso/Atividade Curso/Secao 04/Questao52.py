"""
Calcular valor dos premio e quanto sera dividido entre eles
"""

# Entrada do user
valor_premio = float(input("Valor do Premio: "))
amigo1 = float(input("Valor do investimento: "))
amigo2 = float(input("Valor do investimento: "))
amigo3 = float(input("Valor do investimento: "))

valor_launch = 100 # valor para participar

if amigo1 < valor_launch and amigo2 < valor_launch and amigo3 < valor_launch:
    por_inves1 = amigo1 / valor_launch
    por_inves2 = amigo2 / valor_launch
    por_inves3 = amigo3 / valor_launch

# Calcular quanto cada um vai ficar do premio
    ganhador1 = valor_premio * por_inves1
    ganhador2 = valor_premio * por_inves2
    ganhador3 = valor_premio * por_inves3

# Saida de quanto cada um vai ficar no final
    print(f"O Primeiro fica com R${ganhador1:,.2f}.")
    print(f"O Segundo fica com R${ganhador2:,.2f}.")
    print(f"O Terceiro fica com R${ganhador3:,.2f}.")
else:
    print("Tente novamente")