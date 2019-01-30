#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Removendo números ímpares da listas. """


def purify(lista):
    is_even = []
    for num in lista:
        if (num % 2 != 0):
            is_even.append(num)
    return is_even

print(purify([2, 5, 6, 7, 9, 12, 13]))
