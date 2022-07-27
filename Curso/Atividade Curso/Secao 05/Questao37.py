"""

"""

#Entrada do user - Entrada de usuario
chegada = input("Horario de Entrada: ")# usar-se --> 00:00 ->> : para o programa separar
saida = input("Horario de Saida: ")# usar-se --> 00:00 ->> : para o programa separar

#Fazer separação de string - usando split()
chegada2 = chegada.split(':')
saida2 = saida.split(':')

#Pegar o local do char (string)
hora_chegada = chegada2[0] + chegada2[1]
hora_chegada = int(hora_chegada)#converter string para int

#Pegar o local do char (string)
hora_saida = saida2[0] + saida2[1]
hora_saida = int(hora_saida)
print(hora_saida)

#Calcular o horario e o valor a pagar
tempo_decorrido = (hora_chegada - hora_saida) * -1
print(tempo_decorrido)
if 100 <= tempo_decorrido <= 200:
    print(f'Valor a pagar: R${(tempo_decorrido/100)*1}')