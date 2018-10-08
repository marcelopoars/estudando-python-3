#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo 2 - Intrução break. """

# A instrução "break" interrompe todos os cilcos
# de um laço de repetição

print("Antes de entrar no laço de repetição")
for item in range(10):
    print(item)
    if (item == 66):
        # A instrução "break" encerra o programa
        break
print("Condição do if é falsa")
