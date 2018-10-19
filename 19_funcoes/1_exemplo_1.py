#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Estudando funções no Python. """


# esta função imprime um texto
# não foram definidos "parâmentros"
def imprime_algo():
    print("Minha primeira função, imprime um texto.")


# criando uma função para apresentar o título entre linhas
def titulo(texto):
    print("-" * 50)
    print(texto)
    print("-" * 50)


# chamando a função "imprime_algo()"
# não foi passado "argumento"
imprime_algo()

# chamando a função "titulo()"
titulo("TÍTULO 1 - Estudando funções")
titulo("TÍTULO 2 - Aprendendo a programar em Python")
