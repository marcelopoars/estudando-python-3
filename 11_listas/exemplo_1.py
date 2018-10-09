#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Trabalhando com listas. """

# Uma lista tem seus elementos delimitados por "[ ]" (colchetes)
# Adicionando itens a lista
lista_de_compras = ["pão", "presunto", "queijo", "café", "leito"]
print("=== Exemplo 1 = Minha lista de compras ===")
# Imprimindo a lista por inteiro
print(lista_de_compras)

print("=== Exemplo 2 = Minha lista de compras ===")
# Imprimindo a lista utilizando FOR
for item in lista_de_compras:
    print(item)

print("=== Exemplo 3 = Minha lista de compras ===")
# Imprimindo o primeiro item da listas (no índice 0)
# Toda lista inicia em 0 (zero)
print(lista_de_compras[0])
# Imprime o item no índice "3"
print(lista_de_compras[3])
