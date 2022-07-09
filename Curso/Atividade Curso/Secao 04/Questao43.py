"""
Vendas e descontos
"""

# Entrada de dados
valor_compra = float(input("Valor da compra: "))

desconto = valor_compra-(valor_compra*0.10)
parcelado = valor_compra/3
comissao_vendedor = 0.05*desconto
comissao_vendedor_total = 0.05*valor_compra

print(f"O valor a pagar á vista é de R${desconto:,.2f}.")
print(f"R${valor_compra:,.2f} em 3x fica por R${parcelado:,.2f}.")

print(f"Comissao do vendedor a vista é de R${comissao_vendedor:,.2f}.")

print(f"Comissao do vendedor a parcelado em 3x é de R${comissao_vendedor_total:,.2f}")