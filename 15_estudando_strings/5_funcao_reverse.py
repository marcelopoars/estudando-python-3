#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Finção reverse(). """

"""
Criando uma função para imprimir uma string na ordem inversa.
"""


def reverse(text):
    word = ""
    l = len(text) - 1
    print("Passo 1")
    while l >= 0:
        word = word + text[l]
        l -= 1
        print("Passo 2")
    print("Passo 3")
    return word

print(reverse("Olá"))
