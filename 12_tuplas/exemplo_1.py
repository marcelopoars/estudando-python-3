#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo1 - Estudando TUPLAS. """

# elementos delimitados por um "par de parenteses"
# são para o Python uma "Tupla"
tupla1 = (11, 22, 33, "tt")

# elementos separados por "vírgula"
# são para o Python uma "Tupla"
tupla2 = "aaa", 1, True

# A função "tuple()" converte a string para tupla
tupla3 = tuple("Python")

# inicializando uma tupla vazia
tupla4 = ()
tupla4 = tupla1

# imprimindo o conteúdo das tuplas
print(tupla1)
print(tupla2)
print(tupla3)
print(tupla4)

# imprimindo o tipo da variavel
print(type(tupla1))
print(type(tupla2))
print(type(tupla3))
print(type((1, 2, 3)))
