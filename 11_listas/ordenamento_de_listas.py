#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Ordenamento de listas. """

# vamos novamente popular a lista
lista = ['açúcar', 'pão', 'presunto-magro', 'queijo', 'café', "arroz", "massa", "tomate"]
print(lista)

# Invertendo a lista utilizando a função "reverse()"
lista.reverse()
print(lista)

# ordenando a lista de forma ascendente / função "sort()"
lista.sort()
print(lista)

# outra forma de inverter a lista
lista.sort(reverse = True)
print(lista)
