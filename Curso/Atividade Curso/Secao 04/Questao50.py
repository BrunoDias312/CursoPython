"""
Encontrar o ano em que a pessoa nasceu
"""

idade = int(input("Idade atual: "))
ano_atual = 2022

ano_nascimento = ano_atual - idade

if ano_nascimento < 0:
    ano_nascimento *= -1
    print(f"Com a idade de {idade} anos, o ano de nascimento é ano {ano_nascimento} A.C.")

else:
    print(f"Com a idade de {idade} anos, o ano de nascimento é {ano_nascimento}.")