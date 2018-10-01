#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Exercícios utilizando  o comando WHILE. """

"""
-  primeiro - declarar uma variável para o teste
- cada variavel criada servirá para um determinado teste
sintaxe:
variavel = inicializada conforme o tipo de dado
while + c0mparação + :
    bloco de código
"""

# repetir a pergunta para o usuario: Deseja continuar?
# ler resposta do usuario - via teclado
# dependendo da opção do usuario siga ou não
continua = True
while continua == True:
    resposta = input("Deseja continuar? S / N: ").lower()
    if resposta == "s":
        continua = True
    else:
        continua = False
print("Até mais!!!")
