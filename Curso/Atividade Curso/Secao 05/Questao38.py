"""

"""

# Entrada do user - Entrada de datas
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

data_valida = False
ano_atual = 2022

#Meses de 31 dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        data_valida = True

#Meses de 30 dias
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <=30:
        data_valida = True

elif mes == 2:
    #Testar se é ano bissexto
    if ano%4==0 and ano%100!=0 or ano%400==0:
        if dia <= 29:
            data_valida = True
    elif dia <= 28:
        data_valida = True

if ano < ano_atual:
    if data_valida:
        print("Data valida")
    else:
        print("Data Invalida")

