#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Estudando funções no Python. """

# criando uma função para apresentar o título entre linhas
def titulo(texto):
    print("-" * 50)
    print(texto)
    print("-" * 50)


# criando uma função para somar dois números
def soma(a, b):
    print(f"a = {a} e b = {b}")
    s = a + b
    print(f"A soma de a + b == {s}")


titulo("SOMA DOIS NÚMEROS")
soma(4, 5)
soma(8, 9)
soma(2, 1)
