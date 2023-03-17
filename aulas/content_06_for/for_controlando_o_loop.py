#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" FOR - Controlando o loop. """

numbers = [1, 3, 4, 7]
for number in numbers:
    if number > 6:
        print(number)
print("We printed 7.")


print("=== Exemplo 2 ===")
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for item in a:
    if item % 2 == 0:
        print(item)
