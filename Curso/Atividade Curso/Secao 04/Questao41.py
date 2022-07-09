"""
Valor hora de trabalho em real

Depois colocar as horas trabalhados por mês e calcular o quanto deve
pagar no mes o funcionario;
"""
# Entrada de dados
valor_hora = float(input("Valor Hora: "))
horas_trabalhadas = float(input("Horas Trabalhadas no mês: "))

# Processamento
valor_pagar = (horas_trabalhadas * valor_hora)
valor_pagar = valor_pagar + (valor_pagar*0.10)

print(f"O valor a ser pago ao funcionario é de R${valor_pagar:,.2f} no final do mes.")