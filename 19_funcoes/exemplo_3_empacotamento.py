#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Estudando funções no Python. """

# criando uma função para apresentar o título entre linhas
def titulo(texto):
    print("-" * 50)
    print(texto)
    print("-" * 50)


# criando uma função para contar os números e imprimir
def contador(* numero):
    total = len(numero)
    print(f"Números recebidos: {numero} | Total de números: {total}")


titulo("EXEMPLO 1")
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
