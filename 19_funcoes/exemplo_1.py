#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Estudando funções no Python. """


# esta função imprime uma linha na tela
def mostrar_linhas():
    print("-u" * 25)


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
