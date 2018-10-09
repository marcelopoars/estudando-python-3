#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Interagindo com usuário. """

print("==== Testando o FOR e Função range() ====")
inicio = int(input("Digite o INÍCIO: "))
fim = int(input("Digite o FIM: "))
passo = int(input("Digite o PASSO: "))
loop = [inicio, fim, passo]
for item in range(*loop):
    print(item)

print(type(loop))
