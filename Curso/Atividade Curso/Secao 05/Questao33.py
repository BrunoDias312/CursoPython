"""
Fazer tabela de precos - com novos e antigos preços
"""

entrada_preco = float(input("Valor produto: "))

if entrada_preco <= 80:
    print("Barato")
elif 80 < entrada_preco <= 120:
    print("Normal")
elif 120 < entrada_preco <= 200:
    print("Caro")
elif entrada_preco > 200:
    print("Muito caro")
