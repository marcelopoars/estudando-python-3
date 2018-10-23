#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo 2 - Manipulando arquivos com Python. """

# O método 'readlines()' retorna uma lista com
# cada linha do arquivo. """
# # for i in arquivo.readlines():
# #     print(i, end="")


# Esta função cria um novo arquivo
def criar_arquivo():
    arquivo = open("novo_arquivo.txt", "w")
    arquivo.close()
    # return arquivo


# # esta função escreve no arquivo
def escrever_no_arquivo():
    arquivo = open("novo_arquivo.txt", "w")
    texto = input("\nDigite um texto: ")
    arquivo.write(texto)
    arquivo.close()
    return arquivo


def ler_arquivo():
    arquivo = open("novo_arquivo.txt", "r")
    print("CONTEÚDO DO ARQUIVO\n{}".format(arquivo.read()))
    arquivo.close()
    # return arquivo


""" Testando as funções """
criar_arquivo()
escrever_no_arquivo()
ler_arquivo()
