#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Iterando listas em Python. """

# Iterando listas em Python (imprimindo lista)
lista_numeros = [100, 200, 300, 400]

print("==== Exemplo 1 ====")
for item in lista_numeros:
    print(item)

# Criamos uma nova lista com o mesmo "range"
lista_indice = [0, 1, 2, 3]
print("==== Exemplo 2 ====")
for item in lista_indice:
    lista_numeros[item] += 1000
print(lista_numeros)

print("==== Exemplo 3 ====")
lista_numeros = [100, 200, 300, 400, 500, 600, 700, 800]

for item in range(len(lista_numeros)):
    lista_numeros[item] += 1000
print(lista_numeros)

print("==== Exemplo 4 ====")
lista = ['hello', 'world', 'hi', 'earth']
for word in lista:
    print(word)

print("==== Exemplo 5 ====")
lista = ['hello', 'world', 'hi', 'earth']
for i in range(0, len(lista)):
    print(lista[i])

print("==== Exemplo 6 ====")
lista = ['hello', 'world', 'hi', 'earth']
i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1
