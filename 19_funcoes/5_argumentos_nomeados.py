#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Funções: Argumento posicionais. """

"""
ARGUMENTOS NOMEADOS:
Passagem de valores utilizando "chave e valor".
"""


def dados_pessoais(nome, sobrenoma, idade, sexo):
    print("Nome: {}\nSObrenome: {}\nIdade: {}\nSexo: {}".format(
        nome, sobrenoma, idade, sexo))


# chamando a função e passando a chave + valor
dados_pessoais(nome="João", sobrenome="Silva", idade=30, sexo="H")
