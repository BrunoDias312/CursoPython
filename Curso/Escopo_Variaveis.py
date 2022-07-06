"""
Escopo de variaveis

Dois casos de escopo:

1 - Variaveis globais;
    - Variaveis globais são reconhecidas,ou seja, seu escopo compreende, todo o programa.

2 - Variaveis locais;
    - Variaveis locais são reconhecidaas apenas no bloco onde foram declaradas, ou seja, seu escopo
    esta limitado ao bloco onde foi declarado.

Para declarar variaveis em python fazemos:

nome_da_Variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que
ao declararmos uma variavel, nos não colocamos o dado dela.
Este tipo é inferido ao atribuirmos o valor á mesma

Exemplo em C

int numero = 5;

Exemplo java

int numero = 10;


"""

numero = 42 # Exemplo de variavel global
print(numero)
print(type(numero))

# Isto é permitido apenas por que o python faz uma re-atribuição na variavel. O mesmo nao funcionaria no Java ou C
numero = "Ola mundo"
print(numero)
print(type(numero))

nao_existe = "oi"
#print(nao_existe)

numero = 10
novo = 0

if numero > 10:
    novo = numero + 10
    print(novo)#variavel local - significa que ela nao vai funcionar depois que sair do if em que ela foi declarada

#print(novo) - 
