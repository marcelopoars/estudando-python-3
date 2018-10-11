#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Fatiando listas. """

"""
=================
Inicializando a lista já populada com uma string
lista = ["P", "Y", "T", "H", "O", "N"

  0    1    2    3     4     5    6
[P] [Y] [T] [H] [O] [N] [3]
-7   -6    -5   -4   -3   -2   -1

lista = [x : y : z]
x = start (início)  - valor padrão (0)
y = stop (fim)      - valor padrão (len())
z = step (passo)   - valor padrão (1)
lista[ start : stop : step ]
=================
"""

#Indice: 0      1      2     3      4     5    6
lista = ["P", "Y", "T", "H", "O", "N", 3]

# Imprimindo o elemento zero (0)
print(lista[ 0 ])

# Não definimos posição inicial
# Definimos a posição final
print(lista[ :2 ])

# Definimos a posição inicial
# Não definimos posição final
print(lista[ 2: ])

# Não definimos posição inicial
# Não definimos posição final
# Definimos passo "2"
print(lista[ ::2 ])

# Definimos a posição inicial
# Não definimos posição final
# Definimos passo "2"
print(lista[ 2::2 ])

# Não definimos posição inicial
# Não definimos posição final
# Definimos passo "-1"
# Será impressa a lista ao contrário
print(lista[ ::-1 ])
