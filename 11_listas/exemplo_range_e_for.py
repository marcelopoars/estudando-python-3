#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Utilizando o FOR e função range()."""

print("==== Exemplo 1 ====")
for i in range(10):
    print(i)

print("==== Exemplo 2 ====")
for i in range(0, 10, 2):
    print(i)

print("==== Exemplo 3 ====")
start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    square_list.append(x ** 2)
    square_list.sort()
print(square_list)
