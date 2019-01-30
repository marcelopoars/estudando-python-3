#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Função censor(). """

"""
Criando uma função subtituir uma palavra por asteriscos.
"""

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

print(censor("Programar em python é legal, pq python é legal.", "python"))
