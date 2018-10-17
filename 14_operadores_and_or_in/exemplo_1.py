#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Operadores AND, OR e IN. """

print("==== Exemplo 1 ====")
lista = ["pão", "presunto", "queijo", "café", "leite"]
print("pão" and "leite" in lista)
print("pão" and "macarrão" in lista)

print("==== Exemplo 2 ====")
print("macarrão" in lista)
print(("macarrão" or "leite") in lista)
print(("pão" or "leite") in lista)
print(lista)

print("==== Exemplo 3 ====")
# será retornado falso "False"
# pois a primeira expressão retorna "False"
# sendo assim, o Python encerra o teste
# e não continua resolvendo as próximas expressões
print((("pão" and "macarrão") or ("pão" and "leite")) in lista)
