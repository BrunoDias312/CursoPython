"""
Cardapio - De acordo com o codigo e com a quantidade fazer a cobranca para o cliente.
"""

#Menu para o usuario escolher a opcao desejada
print("<--------------------MENU----------------------->")
print(" ESPECIFICAÇÃO   -  CODIGO  - PRECO PRODUTO")
print(" Cachorro Quente - COD: 100 - VALOR: R$1,20")
print(" Bauru Simples   - COD: 101 - VALOR: R$1,30")
print(" Bauru com Ovo   - COD: 102 - VALOR: R$1,50")
print(" Hamburguer      - COD: 103 - VALOR: R$1,20")
print(" Cheeseburgue    - COD: 104 - VALOR: R$1,70")
print(" Suco            - COD: 105 - VALOR: R$2,20")
print(" Refrigerante    - COD: 106 - VALOR: R$1,00")
print("<----------------------------------------------->\n")

#Entrada para o user
produto_cod = int(input("Cod Produto -> "))
quantidade_produto = int(input("Quantidade: "))
print("<\n----------------------------------------------->\n")

#Seleção
if produto_cod == 100:#Cachorro Quente
    valor_produto_final = 1.20 * quantidade_produto
    print("Produto escolhido: Cachorro Quente")
    print("Preço unitario: R$1,20")
    print(f"Quantidade: {quantidade_produto}")
    print(f"Valor total: R${valor_produto_final:,.2f}")

elif produto_cod == 101:#Bauro Simples
    valor_produto_final = 1.30 * quantidade_produto
    print("Produto escolhido: Bauro Simples")
    print("Preço unitario: R$1,30")
    print(f"Quantidade: {quantidade_produto}")
    print(f"Valor total: R${valor_produto_final:,.2f}")

elif produto_cod == 102:#Bauro com Ovo
    valor_produto_final = 1.50 * quantidade_produto
    print("Produto escolhido: Bauro com Ovo")
    print("Preço unitario: R$1,50")
    print(f"Quantidade: {quantidade_produto}")
    print(f"Valor total: R${valor_produto_final:,.2f}")

elif produto_cod == 103:#Hamburguer
    valor_produto_final = 1.20 * quantidade_produto
    print("Produto escolhido: Hamburguer")
    print("Preço unitario: R$1,20")
    print(f"Quantidade: {quantidade_produto}")
    print(f"Valor total: R${valor_produto_final:,.2f}")

elif produto_cod == 104:#Cheeseburguer
    valor_produto_final = 1.70 * quantidade_produto
    print("Produto escolhido: Cheeseburguer")
    print("Preço unitario: R$1,70")
    print(f"Quantidade: {quantidade_produto}")
    print(f"Valor total: R${valor_produto_final:,.2f}")

elif produto_cod == 105:#Suco
    valor_produto_final = 2.20 * quantidade_produto
    print("Produto escolhido: Suco")
    print("Preço unitario: R$2,20")
    print(f"Quantidade: {quantidade_produto}")
    print(f"Valor total: R${valor_produto_final:,.2f}")

if produto_cod == 106:#Refrigerante
    valor_produto_final = 1.00 * quantidade_produto
    print("Produto escolhido: Refrigerante")
    print("Preço unitario: R$1,00")
    print(f"Quantidade: {quantidade_produto}")
    print(f"Valor total: R${valor_produto_final:,.2f}")