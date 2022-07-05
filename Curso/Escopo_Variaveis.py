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
ao declararmos uma variavel, nos n~]ao colocamos o dado dela.
Este tipo é inferido ao atribuirmos o valor á mesma

Exemplo em C

int numero = 5;

Exemplo java

int numero = 10;


"""

numero = 42
print(numero)
print(type(numero))