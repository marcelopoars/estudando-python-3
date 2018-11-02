#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""SUpermercado."""

prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

for chave in prices:
    print(f"=> {chave} <=")
    print("Preço: ", prices[chave])
    print("Estoque: ", str(stock[chave]))

total = 0
for key in prices:
    total += prices[key] * stock[key]
    print(total)

print(total)


print("=== Fazendo compras ===")


def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
            print(item, " - ", stock[item])
    return total


shopping_list = ["banana", "orange", "apple"]
print(compute_bill(shopping_list))
