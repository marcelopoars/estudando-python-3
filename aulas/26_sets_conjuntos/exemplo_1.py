#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Estudando SETs / conjuntos."

"""
Os conjuntos, diferentes das listas, "não tem ordem",
sendo assim não há "último elemento."
"""

# criando uma lista comum
numeros = [22, 1, 5, 65, 43, 5, 7, 22, 5, 777]
# o conjunto remove "itens repetidos"
numeros_set = set(numeros)
# o método "add()" adiciona um item ao conjunto
numeros_set.add(1000)
# a lista será impressa em uma ordem aleatória
print(numeros_set)

"""Exemplo 02"""
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
print(b)
