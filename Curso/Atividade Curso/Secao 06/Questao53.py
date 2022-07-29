"""
para 'n' fazer o chamado triangulo  de Floyd
"""

n = int(input("Entrada: "))
m = 1
for id in range(1, n+1):
    for i in range(1, id+1):
        print(m, end= ' ')
        m += 1

    print()
