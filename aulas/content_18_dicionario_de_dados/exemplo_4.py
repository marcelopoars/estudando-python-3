#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Dicionários de Dados."""

inventory = {
  'gold': 500,
  'pouch': ['flint', 'twine', 'gemstone'],
  'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

inventory['pouch'].sort()

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['gold'] += 50
print("==== ANTES ====")
print(inventory)
inventory['backpack'].remove('dagger')
print("==== DEPOIS ====")
print(inventory)
