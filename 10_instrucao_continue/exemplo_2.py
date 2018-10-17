#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo 2 - Intrução continue. """

# A intrução "continue" interrompe a execussão de um único ciclo de Loop
# Finaliza somente o ciclo que está sendo executado

print("Início")
i = 0
while (i < 10):
    i += 1
    if (i % 2 == 0):
        #  Se resultar verdadeiro, retorna ao início
        continue
    if (i > 5):
        break
    # Se IF resular falso, será impresso o valor de "i"
    print(i)
if (i > 5):
    print(i, "é maior que 5")
else:
    print("Executa o else")
print("Fim")
