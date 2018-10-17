#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo 1 utilizando WHILE. """

# primeiro - declarar uma variável para o teste
# cada variavel criada servirá para um determinado teste
# sintaxe:
# variavel = inicializada conforme o tipo de dado
# while + comparação + :
#     bloco de código

"""
##### EXEMPLO 1 ####
- repetir a pergunta para o usuario: Deseja continuar?
- ler resposta do usuario - via teclado
- dependendo da opção do usuario siga ou não
"""

# Inicializada a variável (x)
x = 0
# Enquanto o x for menor ou igual a 10
while (x <= 10):
    # Imprime o valor de x
    print(x)
    # A cada repetição x recebe (+1)
    x += 1
