"""
Mostrar a soma de 50 numeros pares
"""
qtd = 50
index = 0

while index < qtd+1:
    if index % 2 == 0:
        print(f"{index}")
    index+=1