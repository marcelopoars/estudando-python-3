#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sintaxe de Compreensão de Lista """

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
print(doubles_by_3)

even_squares = [x * x for x in range(1, 11) if (x * x) % 4 == 0]
print(even_squares)
