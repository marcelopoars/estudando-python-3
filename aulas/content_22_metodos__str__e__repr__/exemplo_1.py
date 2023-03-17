#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" testes. """


class Binario(object):

    def __init__(self, valor_dec):
        """ Método chamado para inicialização do objeto. """
        self.valor_dec = valor_dec
        # A função "bin()" converte decimal em binário
        self.valor_bin = bin(self.valor_dec)

    def __repr__(self):
        """ Método chamado pela função str() para obter o valor
        do objeto em forma de string. """
        return "{} em binário é {}".format(self.valor_dec, self.valor_bin[2:])


if __name__ == "__main__":
    a = Binario(1)
    b = Binario(40)
    print("Convertendo DECIMAL para BINÁRIO")
    print(a)
    print(b)

    # print("\nOutros testes")
    # print(type(b))
    # print(bin(5))
    # print(b.valor_dec)
    # print(b.valor_bin[2:])
    # print(type(Binario(5)))
