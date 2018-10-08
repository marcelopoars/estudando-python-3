#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo 3 - Utilizando FOR e LISTAS. """

# Criar uma lista simples de dados e mostrar dados utilizando for
lista_de_compras = [ "pão", "presunto", "leite", "queijo", "banada" ]
 # for + 01 ou mais variáveis in(da sintaxe) + minha lista (ou outra coisa) + (:) sempre
 #    ... aqui vai o bloco de código
for item in lista_de_compras:
    print("- {}".format(item))

# Mostrar números de 0 até 20
# for + contador + in + range(inicio, fim, passos):
#     ... aqui vai o bloco de código
contador = 0
for numero in range(0, 21, 1):
    print("- {}".format(numero))
    contador += 1
print("Foram digitados: {} númros.".format(contador))
