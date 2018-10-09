#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Trabalhando com listas. """

# Começamos declarando nossa variável do tipo (lista)
# Podemos dar qualquer nome para nossa lista

print("==== Exemplo 1 ====")
for item in list(range(10)):
    print(item)
print(type(list(range(10))))

print("==== Exemplo 2 ====")
lista_1 = list(range(10))
print(lista_1)
print(type(lista_1))

print("==== Exemplo 3 ====")
lista_2 = range(10)
print(lista_2)
print(type(lista_2))
