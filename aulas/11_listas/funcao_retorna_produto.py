#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Esta função retorna o produto de uma lista de inteiros. """


def product(lista):
    prod = 1
    for num in lista:
        prod *= num
    return prod

print(product([2, 5, 4]))
