#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Aula 20  a 21 - Tomada de decisoes utilizando IF, ELIF e ELSE
Ex:
if (True):
    realizar esta tarefa
elif (True):
    realizar esta tarefa
else:
    realizar esta tarefa / ou sair
"""

# print("\n ======== Efetuando testes ========")
# a = 10
# if (a == 10):
#     print("O valor é igual a 10.")
# else:
#     print("O valor não é igual a 10.")

print("\n ======== Perguntando ao usuário ========")
acao = (input("Digite [1] para SIM ou [2] para NÃO: "))
if acao == "1":
    print("Você disse SIM!")
elif acao == "2":
    print("Você disse NÃO!")
else:
    while acao != "1"  and  acao != "2":
        acao = (input("Tente novamente! \n Digite [1] para SIM ou [2] para NÃO: "))
        if acao == "1":
            print("Você disse SIM!")
        elif acao == "2":
            print("Você disse NÃO!")

# print(type(acao))
