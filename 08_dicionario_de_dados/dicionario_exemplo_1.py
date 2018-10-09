#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Dicionário de dados. """

# Imprimir utilizando um DICIONARIO
# Criamos um dicionario chamado: dados_do_usuarios
dados_do_usuarios = {
"nome_usuario" : "João da Silva",
"user_name" : "joaosilva",
"senha" : 232323
}
# Imprime o conteudo do meu dicionario ("dados_do_usuarios")
print("Olá {nome_usuario}! Seu User Name é: {user_name} e sua senha é {senha}" .format(**dados_do_usuarios))
