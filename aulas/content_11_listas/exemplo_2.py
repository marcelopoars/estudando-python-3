#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Trabalhando com listas. """

# Começamos declarando nossa variável do tipo (lista)
# Podemos dar qualquer nome para nossa lista

lista_de_compras = ["pão", "presunto", "queijo", "café", "leite"]
print("Exemplo 1 = Minha lista de compras:")
for item in lista_de_compras:
    # imprime cada item da lista, uma a um
    print(item)

print("Exemplo 2 = Minha lista de compras:")
# Imprime a tista por inteiro
print(lista_de_compras)
lista_de_compras.append("açúcar")
print(lista_de_compras)
lista_de_compras[0] = "Batata"
print(lista_de_compras)
