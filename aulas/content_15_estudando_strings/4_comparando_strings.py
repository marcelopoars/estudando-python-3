#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Comparando Strings. """

"""
O Python disponibiliza 2 funções que são bastante uteis
quando estamos trabalhando com o sistema ASCII.

=> Função ord() - recebe uma letra como parâmetro
    e retorna o código ASCII da mesma.
=> Função chr() - onde passamos o código ASCII
    e nos é retornado a respectiva letra.
"""

# comparando caracteres
# deve retornar (True ou False)
# o Python toma por base o "código na TABELA ACII"
print("a" > "X")
print("a" > "A")
print("a" > "10")

# a função "chr()" retorna o "código" da tabela ASCII
print(chr(100))
print(chr(79))

# a função "ord()" retorna o "caracter" da tabela ASCII
print(ord("d"))

for cod in range(128):
    print(f"- {cod} = {chr(cod)} | Bin: {bin(cod)} | Exa: {hex(cod)}")
