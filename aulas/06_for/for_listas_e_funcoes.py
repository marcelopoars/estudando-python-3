#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" FOR, listas e funções. """


def contar_menores(numeros):
    """Retorna a quantidade de números "menores" que 10."""
    total = 0
    for num in numeros:
        if num < 10:
            total += 1
    return total


# inicializando lista com números
lista = [4, 8, 15, 16, 23, 42]
# chamando a função "encontra_menores"
menores = contar_menores(lista)
print(menores)


# """ EXEMPLO 2 """
def fizz_count(lista):
    count = 0
    for item in lista:
        if item == "fizz":
            count += 1
    return count


lista = ["fizz", "cat", "fizz"]
var = fizz_count(lista)
print(var)
