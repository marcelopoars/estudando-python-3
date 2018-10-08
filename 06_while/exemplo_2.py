#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Exemplo 2 utilizando WHILE. """

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
