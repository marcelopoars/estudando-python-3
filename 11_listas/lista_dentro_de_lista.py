#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Trabalhando com listas. """

# Inicializando uma lista com valores e tipos diversos
lista_1 = ["A", "b", 3, 555, "6", 123]
# Acessando o valor no índice "3"
print(lista_1[3])
# Retorna o tamanho da lista utilizando a função "len()"
print(len(lista_1))
# Aqui temos um lista dentro da lista_2 no índice "0"
lista_2 = [[23, "casa", "x", 76], "a", "b", "c", 77]
# Acessando o conteúdo da lista_2 no indice "0"
print(lista_2[0])
# Retorna o elemento no índice "2"
# da lista que está no índice "0" da lista_2
print(lista_2[0][2])
# Retorna o último elemento da lista_2
print(lista_2[-1])
