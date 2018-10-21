#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Funções: Retorno de valores multiplos. """

"""
O retorno de valores multiplos retorna uma "tupla."
"""


def minha_funcao():
    return 1, 2


def potencia(numero):
    """
    a função retorna o quadrado e o cubo
    de um número
    """
    quadrado = numero ** 2
    cubo = numero ** 3
    return quadrado, cubo


# "a" e "b" recebem os valores
# retornados pela função "minha_funcao()"
a, b = minha_funcao()
print(a, b)

# chamando a função "minha_funcao()"
tupla = minha_funcao()
print(tupla)
print(type(tupla))

# chamando a função "potencia()"
tupla = potencia(3)
print(tupla)
