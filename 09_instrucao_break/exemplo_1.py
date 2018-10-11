#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo 1 - Intrução break. """

# A instrução "break" interrompe todos os cilcos
# de um laço de repetição

print("Antes de entrar no laço de repetição")
for item in range(10):
    print(item)
    if (item == 6):
        print("Condição if é verdadeira")
        # A instrução "break" encerra o loop (FOR)
        break
print("Depois do laço")
