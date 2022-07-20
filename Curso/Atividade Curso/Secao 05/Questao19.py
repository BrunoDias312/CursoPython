"""
Descobrir se um numero é divisivel por 3 ou 5, mas nao simultaniamente pelos os dois
"""

num = int(input("Digite um numero: "))

div3 = num%3
print(div3)
div5 = num%5
print(div5)
print("----------")

if div3 == 0 or div5 == 0:
    if div3 == 0:
        print("Divisivel por 3")
    elif div5 == 0:
        print("Divisivel por 5")
else:
    print("O numero digitado não é divisivel por 3 ou 5.")