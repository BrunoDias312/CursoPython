"""
Declare um menu e de a opcao do user a escolha
"""

print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Difença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

opcao = int(input("Opção: "))

if opcao == 1:
    a = int(input("A: "))
    b = int(input("b: "))
    print(f"A soma de A+B é {a+b}.")
elif opcao == 2:
    a = int(input("A: "))
    b = int(input("b: "))
    if a > b:
        print("A é maior que B.")
    else:
        print("B é maior que A.")
elif opcao == 3:
    a = int(input("A: "))
    b = int(input("b: "))
    print(f"A multiplicação de A*B é {a*b}.")
elif opcao == 4:
    a = int(input("A: "))
    b = int(input("b: "))
    print(f"A divisão de A/B é {a/b}.")
else:
    print("A opção seleciona é invalida!!!")