"""
Calcular imposto de estados - dar entrada de preco do produto e do estado
Retornar o valor final do produto com o debitante do imposto
"""

#Menu
print("Estados:")
print("1 - MG 7%\n2 - SP 12%\n3 - RJ 15%\n4 - MS 8%")
#Entrada de dados
produto_preco = float(input("Preco do produto: "))
estado = int(input("Estado: "))

#A resposta da escolha do user
if estado == 1:# MG
    produto_final = produto_preco - (produto_preco * 0.07)#calculo para o produto

    print(f"R${produto_final:,.2f}")#Saida

elif estado == 2:# SP
    produto_final = produto_preco - (produto_preco * 0.12)

    print(f"R${produto_final:,.2f}")

elif estado == 3:# RJ
    produto_final = produto_preco - (produto_preco * 0.15)

    print(f"R${produto_final:,.2f}")

elif estado == 4:# MS
    produto_final = produto_preco - (produto_preco * 0.08)

    print(f"R${produto_final:,.2f}")

else:
    print("Opção não disponivel.")