#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Classes e Objetos em Python - Cartas. """


class Carta:
    lista_de_naipes = ["Paus", "Ouros", "Copas", "Espadas"]
    lista_de_posicoes = ["narf", "Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Rainha", "Rei"]

    def __init__(self, naipe=0, posicao=0):
        self.naipe = naipe
        self.posicao = posicao

    def __str__(self):
        return (self.lista_de_posicoes[self.posicao] + " de " +
                self.lista_de_naipes[self.naipe])


carta1 = Carta(1, 9)
carta2 = Carta(1, 3)
print(carta1)
print(carta2)
