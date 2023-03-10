#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Dicionários de Dados."""

"""
Operadores de Identidade
is     - avalia se ambos os lados têm a mesma identidade
is not - avalia se ambos os lados têm identidades diferentes
"""

# as chaves podem ser de qualquer tipo imutável
elementos = {
    # chave:    valor
    # neste exemplo as chaves são "Strings"
    'hidrogenio': 1,
    'helio': 2,
    'carbono': 6
}

# adicionando um novo item
elementos['litio'] = 3
print(elementos)

# verificando se a chave "oxigenio" está no dicionário
print('oxigenio' in elementos)
# o método "get()" procura por valores no dicionário
print(elementos.get('oxigenio'))

# imprime o valor referente a chave "helio"
print(elementos["helio"])
