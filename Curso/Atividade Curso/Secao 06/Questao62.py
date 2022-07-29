"""

"""

from num2words import num2words

total = ""

for n in range(1, 1001):
    num = num2words(n, lang='pt-BR')
    total += num.replace(' ', '')

print(f'Entre 1 e 1000 temos {len(total)} letras.')