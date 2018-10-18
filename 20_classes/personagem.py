#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Criando a classe personagem. """


# Criando a classe "Personagem"
# Método construtor
class Personagem:
    def __init__(self, nome, altura, largura, cor, x, y):
        # Atribuindo valores aos atributos da minha classe
        # self._nome é um atributo privado
        #  os demais são públicos
        self._nome = nome
        self.altura = altura
        self.largura = largura
        self.cor = cor
        self.x = x
        self.y = y
        self.vida = "Está vivo"  # vivo

    def __repr__(self):
        # Criando uma representação para o objeto
        return f"Nome: {self._nome} Altura: {self.altura} Largura: {self.largura} Cor: {self.cor} Vida: {self.vida}"

    def andar_para_direita(self):
        self.x += 5
        print("Andei para direita")
        print("Onde estou na posição: {} x {}".format(self.x, self.y))

    def andar_para_esquerda(self):
        self.x -= 5
        print("Andei para esquerda")
        print("Onde estou na posição: {} x {}".format(self.x, self.y))

    def andar_para_baixo(self):
        self.y += 5
        print("Andei para baixo")
        print("Onde estou na posição: {} x {}".format(self.x, self.y))

    def andar_para_cima(self):
        self.y -= 5
        print("Andei para cima")
        print("Onde estou na posição: {} x {}".format(self.x, self.y))

    def falar(self, texto):
        return "{} falou: {} ".format(self._nome, texto)

    def morrer(self, atirou):
        if atirou is True:
            self.vida = "Está morto"
        else:
            self.vida = self.vida
