"""
Fazer um programa que obedeça varias requesitos pedido pelo exercicio
"""


# Inicio da função Soma
def soma(valor_a, valor_b):
    resultado = valor_a + valor_b
    return print(f"Soma: {resultado}")


# Fim da Função Soma

# Inicio da função Média
def media(valor, qtd_entradas):
    resultado = valor / qtd_entradas
    return print("Media:", resultado)


# Fim da Função Média

# funcao media dos pares
def media_pares(valor_a, valor_b):
    par = 0
    qtd_chamada = 0

    if valor_a % 2 == 0:
        par = valor_a
        qtd_chamada += 1

    if valor_b % 2 == 0:
        par = par + valor_b
        qtd_chamada += 1

    media = par / qtd_chamada
    print("Media de pares: ", media)


# Fim Funcao media_pares

# inicio Funcao
contador_q = 0


def quantidade():
    global contador_q
    contador_q += 1


# Fim funcao Quantidade


# Inicio da Função maior_menor
"""
Função para encontrar o maior numero digitado e
    o menor numero digitado.
Funcao dara saida para o user
"""
cont = 0
cont2 = 0
maior = 0
menor = 0


def maiormenor():
    x = 0
    global cont
    global cont2
    global maior
    global menor

    while True:

        valor_a = int(input("Valor A: "))
        quantidade()
        valor_b = int(input("valor B: "))
        quantidade()
        #
        cont += 1
        cont2 += 1

        if cont == 1:
            if valor_a > valor_b:
                maior = valor_a
                menor = valor_b
            else:
                maior = valor_b
                menor = valor_a
        else:
            if valor_a > valor_b:
                maior = valor_a
                menor = valor_b
            else:
                maior = valor_b
                menor = valor_a

        s = int(input("\nSair (0): "))
        print("\n<------------------------>\n")
        if s == 0:
            break

    soma(valor_a, valor_b)
    media(valor_a, valor_b)
    media_pares(valor_a, valor_b)
    print("quantidade de numeros é ", contador_q)
    print(f'O MAIOR número digitado foi {maior}.')
    print(f'O MENOR número digitado foi {menor}.')


maiormenor()#Chamada principal

