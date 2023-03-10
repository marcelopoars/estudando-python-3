#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Expressoes matematicas. """

# Soma
print(10 + 10)
print(10 + (50 + 50))  # atencao a precedencia de operadors
print(10 - 10)
print(1000 - 80)


# Divisao
"""
1 - Quando você divide um inteiro por outro inteiro,
    o resultado é sempre um inteiro (arredondado para baixo, se necessário).
2 - Quando você divide um float por um inteiro, o resultado é sempre um float.
3 - Para dividir dois inteiros e acabar com um float,
    você deve primeiro usar float () para converter um dos inteiros em float.
"""
5 / 2
# 2
5.0 / 2
# 2.5
float(5) / 2
# 2.5


# resultado ignora as casas decimais / retorna inteiro
print(10 // 6)
var = 10//6
print(type(var))
print(type(10/6))

# Modulo da divisao (resto da divisao)
print(3 % 2)
print(4 % 2)
print(5 % 2)
print(7 % 3.1)

# Multiplicacao
print(10 * 8000)
print(55 * 5)

print("=======  Exercício - MÓDULO ========")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

divisao = num1 / num2
resto = num1 % num2

print("- {} dividido por {} é igual a: {}" .format(num1, num2, divisao))
print("- O resto da divisão entra {} e {} é: {}" .format(num1, num2, resto))
