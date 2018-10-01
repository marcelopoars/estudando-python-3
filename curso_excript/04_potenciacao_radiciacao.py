#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Autla 18 - Estudo de potenciacao e radiciacao """
# importando a biblioteca MATH (funcoes de matemática)
import math

#  Operador de POTENCIA: **
print("- quadrado de 5 = ", 5**2) # 5 elavado a segunda potencia
print("- 2 na oitava potência = ", 2**8) # 2 elevado a oitava potencia
print("- 9 ao quadrado = ", 9 ** 2)
# print(9**1000) # 9 elevado a nona potencia
# A raiz quadrada de um numero e´:
# (numero (elevado a potencia de (1 dividido por 2)))
# Ex: raiz quadrada de 81 = (81**(2/1))
print("- raiz quadrada de 4 = ", 4 ** 0.5)
print("- raiz quadrada de 5 = ", 25 ** 0.5)
print("- raiz quadrada de 9 = ", 9 ** 0.5)
print("- raiz quadrada de 81 = ", (81 ** (1/2)))
print("- raiz cubica de 9 = " , 9 ** (1/3))
print("- raiz cubica de 81 = " , 81 ** (1/3))
print("- 9 elevado ao cubo = ", 9** 3)
print("- raiz quadrada de 729 = ", 729**(1/3))

# mostra lista de funcoes contidas na biblioteca "math"
print("=== Lista de funções - Matemática =====")
print(dir(math))
print("=== FIM da lista =================")

print("=== Testando a biblioteca ===========")
print("O valor de PI é: ", math.pi)
