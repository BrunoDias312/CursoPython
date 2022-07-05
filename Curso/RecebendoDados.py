"""
Recebendo dados do usuario

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Bruno'
- Aspas duplas -> "Bruno"
- Aspas simples triplas -> '''Bruno Dias'''
"""
#- Aspas duplas triplas -> """Bruno"""
0

# Entrada de dados
print("Qual o seu nome? ")
nome = input().title() # Entrada de dados - entrada na variavel nome

idade = input("Qual a sua idade? ")

# Processamento

# Saida de dados
# print("Seja bem vindo(a) %s e sua idade é %s anos" % (nome, idade)) - este metodo é antigo e já caiu em desuso

# Preferivel usar esse
print("Seja bem vindo(a) {0} e a sua idade é {1} anos".format(nome, idade))

print(f"Seja bem vindo {nome}") # Versao atual
'''
Caste é "conversão" de um dado para outro
'''

print(f"O {nome} nasceu em {2022 - int(idade)}")
