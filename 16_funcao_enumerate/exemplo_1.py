#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Função enumerate() em Python. """

# a função "enumerate()" retorna o "indice e o valor"
# contidos em uma "lista, tupla ou string"
tupla = (11, 3, 4, 55, 77)
lista = ["casa", "batata"]
for indice, valor in enumerate(tupla):
    print(f"Índice {indice} - {valor}")

t1 = tuple(enumerate(tupla))[0]
print(t1)
print(tuple(lista)[1])

print(tuple(enumerate(lista[1])))
