"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que
- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '68.89'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "68.89"
- Estiver entre aspas simples triplas -> '''uma string''', ''234''', '''a''', '''True''', '''68.89'''
- Estiver entre aspas duplas triplas ->

O barra n, " /n " ainda é usado no Python da mesmo forma que no C++ ou no Java
"""

nome = """ola mundo"""
print(nome.title())
print(f"O tipo da variavel é {type(nome)}.")

print(nome.upper())

print(nome.split())# Para fazer uma lista de strings
"""
[ 1,   2,   3,   4,   5,   6,   7,   8,   9]
['o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
nome = "ola mundo"
"""

print(nome[0:3])# Chama-se Slice de string
print(nome[4:9])# Faca isto caso queira mostrar apenas determidados caracteres da string list
print(nome.split())# Separa a string por lista -> ['ola', 'mundo']

print(nome[::-1])# comeca pelo primeiro elemento, vai ate o final, e entao inverta os elementos e por fim coloca na tela
