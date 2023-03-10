#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Funções: Parâmetros default. """


# definindo uma função
# com "dois parâmetros"
def login(user="admin", senha="1234"):
    print(f"Usuário: {user}")
    print(f"Senha: {senha}")


# chamando a função "login()"
login()

# chamando a função "login()"
# passando novo argumento "user"
# nome de usuários será alterado
login("Marcelo")

# alterando apenas a senha
login("admin", 54321)
