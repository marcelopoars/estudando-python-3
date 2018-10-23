#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Classe Pessoa. """


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def imprime_dados_pessoa(self):
        print("\nDADOS DO OBJETO PESSOA")
        print("Nome: {}\nSobrenome: {}\nIdade: {}".format(
            self.nome, self.sobrenome, self.idade))

    def teste_maioridade(self):
        if self.idade >= 18:
            print("Esta pessoa é MAIOR de idade.")
        else:
            print("Esta pessoa é MENOR de idade")


pessoa1 = Pessoa("Marcelo", "Pereira", 40)
pessoa1.imprime_dados_pessoa()
pessoa1.teste_maioridade()

pessoa2 = Pessoa("João", "Silva", 15)
pessoa2.imprime_dados_pessoa()
pessoa2.teste_maioridade()
