#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Herança - Exemplo Eletrônicos."""


# Criando classe PAI "Eletronico"
class Eletronico:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def status(self):
        return self.ligado


# Criando classe FILHA "Tv"
class Tv(Eletronico):
    def __init__(self):
        Eletronico.__init__(self)
        self.volume = 0

    def __repr__(self):
        return "Sua [Tv] está {} no volume [{}]".format(
            self.ligado, self.volume)

    def aumentar_volume(self):
        if self.ligado is False:
            print("Sua [Tv] está desligada!")
        else:
            self.volume = self.volume + 1

    def diminuir_volume(self):
        if self.volume is 0:
            print(f"O volume já está é '{self.volume}'")
        else:
            self.volume = self.volume - 1

    def obter_volume(self):
        return self.volume

    def imprimir_status(self):
        print(self.__repr__())


# criando novo objeto tipo "Eletronico"
tv1 = Tv()
tv1.ligar()
tv1.aumentar_volume()
tv1.imprimir_status()
