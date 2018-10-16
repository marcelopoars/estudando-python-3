#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Operadores IN e NOT IN. """

print("==== Exemplo 1 ====")
lista = ["pão", "presunto", "queijo", "café", "leite"]
print("leite" in lista)
print("leite" not in lista)

print("==== Exemplo 2 ====")
x = ( range(1, 10) )
if 3 in x:
    print("3 está contido no range(1, 10)")
else:
    print("3 não está contido no range(1, 10)")

print(x)
print(type(x))
