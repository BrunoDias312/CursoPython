"""
Encontrar valor primo e somar os primos até ele

Lembre-se que 1 nao é primo
procupar um divisor de 2 até a metade do numero. Se exitir pelo menos um nao é primo
se nao encontrar divisor é primo.
"""


def testaPrimo(num):
    # 1 não é primo

    if (num == 1):
        return False

    # Se o loop encontrar um divisor de 2 ate a metade do número.
    for d in range(2, (int)(num / 2) + 1):

        if (num % d == 0):
            return False

        # Se o loop terminar e nao encontrar divisores, o numero é primo
    else:
        return True
# Fim Função

# Chamar user
valor = int(input("Valor de ate onde encontrar primo: "))
    soma = 0

    # Vamos somar todos os primos de 1 a 10
    # 2 + 3 + 5 + 7 = 17
    for i in range(1, valor):
        if (testaPrimo(i)):
            soma += i

    else:
        print(soma)

# Fim Programa

def chamarUser():

chamarUser()