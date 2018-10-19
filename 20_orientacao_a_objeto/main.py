#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Criando objeto personagem. """

# Importando a classe "Personagem"
# Instanciando o "objeto personagem"
from personagem import Personagem
# Passando seu atributos
p = Personagem("Abel", 1, 1, "azul", 5, 5)
p._nome = "João"


# Chamando o método de representação do objeto (p) tipo classe (Persinagem)
print(p.__repr__())

atirou = True
p.morrer(atirou)

print(p.__repr__())

# print(p.falar("Olá"))

# p.andar_para_direita()
# for x in range(3):
#     p.andar_para_cima()
# p.andar_para_esquerda()
# p.andar_para_baixo()
