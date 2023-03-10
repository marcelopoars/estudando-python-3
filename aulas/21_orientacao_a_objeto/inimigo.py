#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Classe inimigo. """


# Criando a classe "Inimigo"
class Inimigo:
    def __init__(self, vida=5):
        self.vida = vida

    def ataque(self):
        print("Eu fui atacado e perdi 01 vida.")
        self.vida -= 1

    def verificar_vida(self):
        if self.vida <= 0:
            print(f"Eu estou morto. [ Total de vidas: {self.vida} ]")
        else:
            print(f"Ainda estou em combate e tenho {self.vida} vida(s).")


# instanciando novos objetos tipo "Classe Inimigo"
inimigo1 = Inimigo()
inimigo2 = Inimigo()
inimigo3 = Inimigo()

inimigo1.ataque()
inimigo1.ataque()
inimigo1.ataque()
inimigo1.ataque()
inimigo1.ataque()

inimigo2.ataque()
inimigo2.ataque()
inimigo2.ataque()

inimigo1.verificar_vida()
inimigo2.verificar_vida()
inimigo3.verificar_vida()
