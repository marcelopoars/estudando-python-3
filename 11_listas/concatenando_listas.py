#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Trabalhando com listas. """

# Inicializando uma lista com valores e tipos diversos
lista = ["A", "b", 3, 555, "6", 123] + [333, "ssss"]

# lista = []
for item in range(5):
    num = int(input("Digite um número: "))
    lista = lista + [num]
print(lista)
