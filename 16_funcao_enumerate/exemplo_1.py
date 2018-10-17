#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Função enumerate() em Python. """

# a função "enumerate()" retorna o "indice e o valor"
# contidos em uma "lista, tupla ou string"
tupla = ("casa", 222, "bolo", 1.33, True)
for indice, valor in enumerate(tupla):
    print(f"Índice {indice} - {valor}")
