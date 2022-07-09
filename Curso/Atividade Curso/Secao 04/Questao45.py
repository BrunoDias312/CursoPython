"""
Transformar Maiuscula em minuscula usando ASCII
"""

# Entrada em letra maiuscula
entrada = input("Digite uma letra(maiuscula): ")

#Processamento
entrada_pre_processada = ord(entrada)
saida = chr(ord(chr(entrada_pre_processada)) + 32)

# Saida de dados
print(saida)