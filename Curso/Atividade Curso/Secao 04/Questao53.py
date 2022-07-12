"""
Calcular o valor de um terreno por CxL e preco da tabela
"""

# Entrada de dados
comprimento = float(input("Entrada do comprimento: "))
largura = float(input("Entrada de largura: "))
valor_imovel = float(input("Entrada de valor por metros²: "))

# Encontrar area
area_imovel = largura * comprimento

preco_area = valor_imovel * area_imovel

# Saida de dados
print(f"O preco por metros² é de R${valor_imovel:,.2f}, o preco que deu "
      f"foi de R${preco_area:,.2f} ao todo.")
