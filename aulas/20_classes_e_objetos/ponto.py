#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Classes e Objetos em Python. """


class ponto:
    pass


def mesmo_ponto(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)


final = ponto()

final.x = 3.0
final.y = 4.0

print(final.x)
print(final.y)

p1 = ponto()
p1.x = 3
p1.y = 4
p2 = ponto()
p2.x = 3
p2.y = 4
print(p1 == p2)
print(id(p1))
print(id(p2))

print(mesmo_ponto(p1, p2))
