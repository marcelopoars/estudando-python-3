#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Esta função remove o número do meio da listas. """


def median(numbers):
    slist = sorted(numbers)
    print(slist)
    nr = len(numbers)
    factor = 1 - nr % 2

    return (float(slist[ int(nr/2 - factor)]) + slist[int(nr/2)])/2

print(median([4, 8, 7, 3, 6]))
