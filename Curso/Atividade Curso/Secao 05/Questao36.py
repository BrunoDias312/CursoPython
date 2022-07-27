"""
Comissão para funcionario de acordo com a tabela
"""

venda_mensal = float(input("Entrada de valor da comissão: "))

if venda_mensal >= 100000:
    comissao = (venda_mensal * 0.16) + 700
    print(f"Comisão: R${comissao:,.2f}")

elif 100000 > venda_mensal >= 80000:
    comissao = (venda_mensal * 0.14) + 650
    print(f"Comisão: R${comissao:,.2f}")

elif 80000 > venda_mensal >= 60000:
    comissao = (venda_mensal * 0.14) + 650
    print(f"Comisão: R${comissao:,.2f}")

elif 60000 > venda_mensal >= 40000:
    comissao = (venda_mensal * 0.14) + 550
    print(f"Comisão: R${comissao:,.2f}")

elif 40000 > venda_mensal >= 20000:
    comissao = (venda_mensal * 0.14) + 500
    print(f"Comisão: R${comissao:,.2f}")

elif venda_mensal < 20000:
    comissao = (venda_mensal * 0.14) + 400
    print(f"Comisão: R${comissao:,.2f}")