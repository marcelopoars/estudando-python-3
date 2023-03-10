#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Funções variádicas. """


# ideal para trabalhar com "listas" ou "tuplas"
def lista_de_argumentos(*args):
    print(args)
    print(type(args))


# ideal para trabalhar com "dicionários"
def lista_de_argumentos_associativos(**kwargs):
    print(kwargs)
    print(type(kwargs))


# ideal para trabalhar com "listas, tuplas ou dicionários"
def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)


# imprime a tupla de argumentos posicionais
lista_de_argumentos(1, 2, 3, 4, 5)
lista_de_argumentos("um", "dois", "três")

# imprime o dicionário de argumentos associados
lista_de_argumentos_associativos(a=11, b=22, c=33, d=44)
lista_de_argumentos_associativos(nome="Marcelo", sobrenome="Pereira")


argumentos(222, 333, 444, 555, nome="João", idade=30)
