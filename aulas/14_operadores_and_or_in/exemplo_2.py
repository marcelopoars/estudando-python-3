#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo 2 - Operadore IN. """

# inicializando variáveis
a = 10
b = 25
c = 66

# solicitando dados do usuário
x = int(input("Digite um número: "))

# efetuando teste
# atribuimos de "a, b, c" a uma lista
if (x in [a, b, c]):
    print("O número digitado está contido.")
else:
    print("O número digitado NÃO está contido.")
