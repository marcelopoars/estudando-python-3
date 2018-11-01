#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Dicionário de dados. """

# Imprimir utilizando um DICIONARIO
# Criamos um dicionario chamado: dados_do_usuarios
usuarios = {
    # chave | valor
    "nome": "João da Silva",
    "user": "joaosilva",
    "senha": 232323
}

# imprime conteúdo do dicionário
print(usuarios)

# retorna o valor referente a chave "nome"
print(usuarios["nome"])

# Imprime o conteudo do meu dicionario ("dados_do_usuarios")
# (**) expande o dicionário
print("Olá {nome}! Seu User é: {user} | Senha é: {senha}".format(**usuarios))

# a função "len()" retorna o tamanho do dicionário
print(f"O dicionário de dados tem {len(usuarios)} elementos.")

# a função "del()" exclui um elemento do dicionário
del(usuarios["nome"])

# agora o dicionário tem apenas "2" elementos
print(usuarios)

# a função "keys()" retorna apenas as chaves do dicionário
print(usuarios.keys())
print(type(usuarios.keys()))

# a função "values()" retorna os valores do dicionário
print(usuarios.values())

# a função "grt()" retorna o valor vinculado a chave informada
print(usuarios.get("user"))

# a função "popitem()" retorna um elemento
# em seguida remove mesmo do dicionário
print(usuarios.popitem())
# chamando a função "popitem()" mais uma vez
print(usuarios.popitem())
# agora o dicionário está vazio
print(usuarios)
