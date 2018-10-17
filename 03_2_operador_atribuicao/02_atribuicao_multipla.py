#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Atribuição multipla. """

# Variável "a" recebe o valor "10"
# Variável "b" recebe o valor "5"
a, b = 10, 5
print("a = ", a)
print("b = ", b)

#  invertendo valores
a, b = b, a
print("Trocando valores de variaveis")
print("a = ", a)
print("b = ", b)

# outro exemplo de atribuição multipla
a, b, c = 2, 4, 8
a, b, c = (a * 2), (a + b + c), (a * b * c)
print("Outro exemplo")
print(a)
print(b)
print(c)

# Exemplo utilizando STRINGS
nome, sobrenome = "Marcelo", "Pereira"
print("Exemplo utilizando STRINGS")
print(nome, sobrenome)
