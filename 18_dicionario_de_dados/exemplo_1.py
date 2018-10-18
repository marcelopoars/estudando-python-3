#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Dicionário de dados. """

# Imprimir utilizando um DICIONARIO
# Criamos um dicionario chamado: dados_do_usuarios
usuarios = {
    "nome": "João da Silva",
    "user": "joaosilva",
    "senha": 232323
}
# Imprime o conteudo do meu dicionario ("dados_do_usuarios")
print("Olá {nome}! Seu User é: {user} | Senha é: {senha}".format(**usuarios))
