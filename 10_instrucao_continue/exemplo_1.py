#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exemplo 1 - Intrução continue. """

# A intrução "continue" interrompe a execussão de um único ciclo de Loop
# Finaliza somente o ciclo que está sendo executado

print("Início")
i = 0
while (i < 10):
    i += 1
    if (i % 2 == 0):
        #  Se resultar verdadeiro, retorna ao início 
        continue
    # Se IF resular falso, será impresso o valor de "i"
    print(i)
else:
    print("Executa o else")
print("Fim")
