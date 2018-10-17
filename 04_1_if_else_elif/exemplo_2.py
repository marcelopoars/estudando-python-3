#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Tomada de decisoes utilizando IF, ELIF e ELSE. """

"""
Ex:
if (True):
    realizar esta tarefa
elif (True):
    realizar esta tarefa
else:
    realizar esta tarefa / ou sair
"""

print("\n ======== Perguntando ao usuário ========")
acao = (input("Digite [1] para SIM ou [2] para NÃO: "))
if acao == "1":
    print("Você disse SIM!")
elif acao == "2":
    print("Você disse NÃO!")
else:
    print("Você disse NÃO digitou nem [1] nem [2].")
