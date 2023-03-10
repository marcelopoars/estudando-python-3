#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Função anti_vowel(). """

def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result

print(anti_vowel("Ola pessoal"))
