#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Utilizando a função "enumerate()". """

print("==== Exemplo | Função enumerate() ====")
lista_numeros = [100, 200, 300, 400, 500, 600, 700, 800]

for index, item in enumerate(lista_numeros):
    lista_numeros[index] += 1000
    print(index, item)
print(lista_numeros)
