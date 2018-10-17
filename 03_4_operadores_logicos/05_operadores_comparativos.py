#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Aula 19 - Operadores comparativos / relacionais
- sao utilizados para verificar CONDIÇOES e julgarem se:
VERDADEIRO (True) ou FALSO (False)
"""
print("=== Os exemplos abaixo retornam sempre TRUE ou FALSE =====")
print("(>)   - maior que ...")
print("(<)   - menor que ...")
print("(>=) - maior ou igual a ...")
print("(<=) - menor ou igual a ...")
print("(==) - igual")
print("(!=) - diferente")

teste_1 = "a" == "a"
teste_2 = "a" == "b"
teste_3 = "a" != "b"
teste_4 = 12 == "12"
print("teste 1 = {} | teste 2 = {} | teste 3 = {} | teste 4 = {}".format(
    teste_1, teste_2, teste_3, teste_4))
