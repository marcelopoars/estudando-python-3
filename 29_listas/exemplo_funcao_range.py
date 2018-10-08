#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Trabalhando com listas e função range(). """
# Aqui são impressas listas em diferentes intervalos
# Utilizo duas funções: list() e range()

# Imprime uma lista de 10 números
# Início: 0  / Fim: 10 / Passo: 1
print(list(range(10)))

# Início: 1  / Fim: 15 / Passo: 5
print(list(range(1, 15, 5)))

# Início: 0  / Fim: 100 / Passo: 10
print(list(range(0, 100, 10)))

# Início: 0  / Fim: 100 / Passo: 3
print(list(range(0, 100, 3)))

# Início: 100  / Fim: 0 / Passo: -3
print(list(range(100, 0, -3)))

# Início: -100  / Fim: 0 / Passo: 3
print(list(range(-100, 0, 3)))
