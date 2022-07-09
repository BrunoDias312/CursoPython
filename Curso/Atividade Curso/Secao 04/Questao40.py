"""
Encanador - valor a ser pago de determinado periodo de dias
8% de imposto de renda
"""

valor_encanador = 30

dias_trabalhados = int(input("Dias trabalhados: "))

valor_bruto = dias_trabalhados * valor_encanador

valor_pagar = valor_bruto - (valor_bruto * 0.08)

print(f"Valor a pagar para o encandor é de R${valor_pagar:,.2f}.")