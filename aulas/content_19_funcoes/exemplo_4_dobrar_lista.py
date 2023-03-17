#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Estudando funções no Python. """


# criando uma função para apresentar o título entre linhas
def titulo(texto):
    print("-" * 50)
    print(texto)
    print("-" * 50)


def dobrar_valores(lista):
    indice = 0
    while indice < len(lista):
        lista[indice] *= 2
        indice += 1
    print(lista)


lista = [6, 3, 9, 1, 0, 2]

dobrar_valores(lista)
