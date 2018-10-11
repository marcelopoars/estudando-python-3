#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Incluindo, alterando e excluindo itens da lista. """

# Vamos inicializar uma lista já populada
lista =["pão", "presunto", "queijo"]
# imprimindo lista inteira
print(lista)
# imprimindo item da posição (1)
print(lista[1])
# vamos inserir um item na lista utilizando função "append()"
# a função "append()" insere um item no final da lista
lista.append("café")
# imprimindo lista inteira
print(lista)
# agora vamos inserir um item na posição (0) da lista
# vamos utilizar a função "insert()"
lista.insert(0, "açúcar")

# conteudo atual da lista
# ['açúcar', 'pão', 'presunto', 'queijo', 'café']
# imprimindo lista inteira
print(lista)

# agora vamos ALTERAR o conteudo de um item da lista
# precisamos informar a posição do item
lista[2] = "presunto-magro"

# # conteudo atual da lista
# ['açúcar', 'pão', 'presunto-magro', 'queijo', 'café']
# imprimindo lista inteira
print(lista)

# vamos apagar todo conteudo de nossa lista
# Utilizamos a função "clear()"
lista.clear()

# imprimindo lista inteira
# agora a lista está vazia
print(lista)

# vamos novamente popular a lista
lista = ['açúcar', 'pão', 'presunto-magro', 'queijo', 'café']
print(lista)

# vamos excluir um elemento da lista
# vamos utilizar a função "pop()"
# por padrão esta função exclui o último elemento da lista
lista.pop()
print(lista)

# podemos escolher a posição do item a ser excluindo
# basta passar como parâmetro da função
# vamos excluir o elemento da posição (0) zero
lista.pop(0)
print(lista)
