"""
Compra com desconto de 12%
"""

compra = float(input("Valor da compra: "))

compra_com_desconto =compra - (compra * 0.12)

print(f"A compra com desconte de 12% fica por R${compra_com_desconto:,.2f}.")