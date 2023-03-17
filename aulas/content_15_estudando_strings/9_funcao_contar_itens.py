#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Finção count(). """

"""
Criando uma função que retorna número de vezes que o item aparece na lista.
"""

def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count

print(count(["mary", 4, 4 , "jon", "bam", 4, 4], 4))
