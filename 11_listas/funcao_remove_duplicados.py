#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Removendo ítens duplicados da listas. """


def remove_duplicates(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

print(remove_duplicates([2, 5, 6, 7, 2, 12, 2]))
