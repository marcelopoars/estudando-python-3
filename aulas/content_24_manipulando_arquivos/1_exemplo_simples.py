#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Manipulando arquivos com Python. """

escrever_no_arquivo = open("arquivo.txt", "w")
escrever_no_arquivo.write("Escrevendo na primeira linha do arquivo.\n")
escrever_no_arquivo.write("Escrevendo na segunda linha do arquivo.")
escrever_no_arquivo.close()

ler_arquivo = open("arquivo.txt", "r")
print(ler_arquivo.read())
ler_arquivo.close()
