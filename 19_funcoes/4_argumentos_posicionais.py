#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Funções: Argumento posicionais. """

"""
ARGUMENTOS POSICIONAIS:
Passagem de valores na ordem como foi implementado na função.
"""


def dados_pessoais(nome, sobrenoma, idade, sexo):
    print("Nome: {}\nSObrenome: {}\nIdade: {}\nSexo: {}".format(
        nome, sobrenoma, idade, sexo))


# chamando a função e passando os valores
dados_pessoais("João", "Silva", 30, "H")
