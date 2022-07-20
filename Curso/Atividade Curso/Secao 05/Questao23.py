"""
Descobir se determinado ano é bisexto
"""

ano = int(input("Entrada do ano: "))

bis = ano%4

if bis == 0:
    bis = ano%100
    if bis != 0:
        print(f"O ano {ano} é bissexto, e consequentemente o mes de fevereiro é de 29 dias")
else:
    print(f"O ano {ano} não é bissexto. Com isso, o mês de fevereiro possui 28 dias")