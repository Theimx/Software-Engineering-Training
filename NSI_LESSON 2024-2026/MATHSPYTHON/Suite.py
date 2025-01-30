from math import *

#This is a File to group my maths Algo that the prof ask us to do in exercise, This file 
#is about The Suite chapters.abs


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