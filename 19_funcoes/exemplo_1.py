#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Estudando funções no Python. """

"""
SINTAXE
def nome_da_funcao():
    bloco de instrução
"""

# esta função imprime uma linha na tela
def mostrar_linhas():
    print("-" * 50)

# criando uma função para apresentar o título entre linhas
def titulo(texto):
    print("-" * 50)
    print(texto)
    print("-" * 50)


# chamando a função "mostrar_linhas()"
mostrar_linhas()

# chamando a função "titulo()"
titulo("TÍTULO 1 - Estudando funções")
titulo("TÍTULO 2 - Aprendendo a programar em Python")
