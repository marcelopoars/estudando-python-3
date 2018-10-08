#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Atribuição condicional - exemplo 02. """

# Inicializada variável (num1)
# Usuário deve digitar um número
# A função "int()" converte o dado digitado para INTEIRO
# A variável "num1" recebe este número digitado e convertido em inteiro
num1 = int(input("Digite um número: "))
# Atribuição condicional
s = "PAR" if num1 % 2 == 0 else "ÍMPAR"
# Imprime resultado utilizando as funções "print()" e ".format()"
print("O número {} é {}" .format(num1, s))
