"""
Aposentadoria - cumprindo os requesitos minimos
Entrar com idade e tempo de trabalho
"""

idade = int(input("Idade: "))
tempo_trabalhado = int(input("Tempo de serviço: "))

if idade >= 65:
    print("Aposentadoria Aceita")
elif tempo_trabalhado >= 30:
    print("Aposentadoria Aceita")
elif idade >= 60 and tempo_trabalhado >= 25:
    print("Aposentadoria Aceita")
else:
    print("Requesitos minimos para aposentadoria não cumprido!!!")