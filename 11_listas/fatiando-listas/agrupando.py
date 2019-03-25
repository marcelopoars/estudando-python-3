#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Teste DELL IT ACADEMY."""

# Lista passada pelos intrutores do teste
# lista_original = [100, 101, 102, 103, 104, 105, 110, 111, 112, 113, 114, 115, 150]

lista_original = [103, 104, 105, 106, 107, 108,  109, 110, 111, 112, 113, 114, 115, 150]

# Aqui crio 3 lista
# Na primeira lista já adiciono o primeiro item da lista original
# As outras listas deix
# o vazias
listas = []
l = []
n = 0

# Aqui crio uma variável para armazenar o valor do número anterior
# Para depois poder comparar com o valor atual dentro do laço "FOR"
anterior = lista_original[0]

# Aqui vou percorrer a lista
for item in lista_original:
    if (item == anterior) or (item == anterior + 1):
        l[n].append(item)
        anterior = item



print("Listas", listas)