"""
Emprestimo - se maior que 20% nao aceitar, caso contrario sim
"""
#entrada do user
salario = float(input("Salario atual: "))
valor_emprestimo = float(input("Valor do emprestimo requerido: "))
qtd_parcela = int(input("Quantidade de parcelas: "))

#calular 20% do salario
cal_salario = salario * 0.2

#calcular parcela do emprestimo
cal_parcela_emprestimo = valor_emprestimo / qtd_parcela

#Verificar se o emprestimo sera aceito
if cal_parcela_emprestimo <= cal_salario:
    print("\nEmprestimo aceito!!!")
    print(f"Valor requerido é R${valor_emprestimo:,.2f}.")
    print(f"Será dividido em {qtd_parcela}x e cada parcela será de R${cal_parcela_emprestimo:,.2f}.")
else:
    print("Emprestimo não aceito")