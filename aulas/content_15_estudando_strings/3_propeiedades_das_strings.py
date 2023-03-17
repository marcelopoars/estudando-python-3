#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Propriedades das Strings. """

"""
ATENÇÃO:
Toda String é uma lista de caracter imutável, ou seja
SEU CONTEÚDO NÃO PODE SER MODIFICADO.
"""

# inicializando uma string
s = "Minha String é uma Lista de Caracteres"

# imprimindo o tamanho da string
print(len(s))

# imprime o caracter da posição "5"
# será impresso um "espaço / vazio"
print(s[5])

# a função "split()" divide a syring em pasrtes
# e retorna uma LISTA
# o parâmentro passado foi o caracter "espaço"
string_dividida = s.split(" ")
print(string_dividida)

# a função "replace()" altera os caracteres
# trocando os "i" por "U"
# é necessário atribuir o resultado para uma NOVA variável
string_alterada = s.replace("i", "U")
print(string_alterada)
