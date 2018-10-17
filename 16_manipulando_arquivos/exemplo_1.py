#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Manipulando arquivos com Python. """


def abre_arquivo_leitura(nome_do_arquivo):
    """ A função abre o arquivo para leitura. """
    arquivo = open(nome_do_arquivo, "r")
    return arquivo


def abre_arquivo_escrita(nome_do_arquivo):
    """ A função abre o arquivo para escrita. """
    arquivo = open(nome_do_arquivo, "w")
    return arquivo


def ler_arquivo(arquivo):
    """ A função lê o arquivo linha por linha e imprime.
        O método 'readlines()' retorna uma lista com
        cada linha do arquivo. """
    for i in arquivo.readlines():
        print(i, end="")


def editar_arquivo(arquivo, texto):
    """ A função 'write()' sobre-escreve arquivo linha por linha. """
    arquivo.write(texto)


meu_arquivo_leitura = abre_arquivo_leitura("arquivo.txt")
ler_arquivo(meu_arquivo_leitura)
print()

meu_arquivo = abre_arquivo_escrita("arquivo.txt")
novo_texto = input("Digite um texto: ")
editar_arquivo(meu_arquivo, novo_texto)

ler_arquivo(meu_arquivo_leitura)
