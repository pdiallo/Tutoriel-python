#!/usr/bin/env python
# -*- coding:utf-8 -*-

#print "Hello World"
 


def somme2(a, b):
    """
     Fait la somme de deux entiers
    """
    c = a + b

    return c



p = somme2(1, 2)
print(p)


def somme4(m, n, h, f):
    """
    Fait la somme de quatre entiers en se basant sur la fonction somm2()
    """
    d = somme2(somme2(m,n), somme2(h,f))
    return d

def somme3(w, x, r):
    d = somme2(somme2(w, x), r)
    return d


v = somme4(1,4, 3, 2)
print(v)

#estPaire = lambda x : (True if (x%2 == 0) else False)

estPaire = lambda x :(x%2 == 0)



# Fonction lambda qui retourne si un nombre est paire ou impaire

def sommeGeneral(*arg):
    """
    Fait la somme de n nombres donnees en parametre (n etant variable)
    """

    s = 0
    for i in arg:
        s = s + i
    return s

s = sommeGeneral(10, 20, 30)

print(s)

x = (2, 4)
y = (3, 4)

import math
def distance(a, b):
    """
    Calcule la distance entre deux points. Le deuxieme point doit etre un parametre facultatif, par defaut il vaut (0,0)
    """

    q = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    return q

x = (3, 4)
y = (3, 4)

q = distance(x, y)
print(q)


