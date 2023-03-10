#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Criar uma função chamada "distancia()"
que calcule a distância entre dois pontos,
dados pelas coordenadas (x1,y1) e (x2,y2).
Dica: TOmar base pelo teorema de Pitágoras:
Ex: distancia = V (x2 - x1)2 + (y2 - y1)2
"""

import math


def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dquadrado = dx ** 2 + dy ** 2
    resultado = math.sqrt(dquadrado)
    print("resultado = ", resultado)
    return 0.0


distancia(1, 2, 4, 6)
