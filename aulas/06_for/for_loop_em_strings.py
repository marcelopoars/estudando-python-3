#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" FOR - loop em Strings. """

for letter in "\nPython":
    print(letter)

print("===================")

strings = "Programar em Python é bem legal!"

for letra in strings:
    # imprime somente a letra "e"
    if letra == "e":
        print(letra)
