from math import *

#Chapter 5 : Suites réelles 
#III Algoritmes et suites récurrentes :

#This is a File to group my maths Algo that the prof ask us to do in exercise, This file 
#is about The Suite chapters.abs

#The Four type of suite Algorithm : 
#
#
#
#

def sommeExo1():
    _w = 3
    _s = _w
    for i in range(5):
        _w = 3*_w -2
        _s += _w
    return(_s)

def sommeExo2(_n):
    _x = 3
    _s = _x
    for i in range(_n):
        _x = 3*_x -2
        _s += _x
    return(_s)

def Example3():
    _N = 1

    while N < 250:
        _N = 2* _N
    print(_N)


def Example2():
    _x = 2
    for i in range(8):
        _x = 3*_x + 5
    print(_x)

#Pour i allant de 1 jusqu'a 20 afficher i².
def Example1():
    
    for i in range(1,21):
        print(i**2)

def arbre():
    x = 32 
    for i in range(1,6):
        x = x * 1.25 - 2
        print(x)
    return(x)

def arbre2(A):
    x = 32 
    n = 0
    while A >= x:
        x = x * 1.25 - 2
        n += 1
        print(n)
        print(x)
    return(n)
