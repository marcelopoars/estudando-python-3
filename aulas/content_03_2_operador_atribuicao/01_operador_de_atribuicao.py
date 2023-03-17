#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Operador de atribuição. """

# =  (sinal utilizado para atribuir um valor a uma variável)
# Ex:
# variavel = 2
# variavel == 2 (True)

print("==== Exemplo 01 ====")
variavel = 2
print(variavel)

print("==== Exemplo 02 ====")
a = 2
b = c = d = a
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))

print("==== Exemplo 03 ====")
e = b == c == d == a
print(e, type(e))
