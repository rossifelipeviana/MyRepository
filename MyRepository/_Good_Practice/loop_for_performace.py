import os
import sys

os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from kdecorator import kdecorator


@kdecorator.timeit
def fun1():
    lista = [1] * 10000000
    for i in range(len(lista)):
        a=i
    return a

@kdecorator.timeit
def fun2():
    lista = [1] * 10000000
    length = len(lista)
    for item in range(length):
        a=item
    return a


@kdecorator.timeit
def fun3():
    lista = [1] * 10000000
    for item in lista:
        a=item
    return a


@kdecorator.timeit
def fun4():
    lista = [1] * 10000000
    for index, item in enumerate(lista):
        a, b = index, item
    return a, b


fun1()
fun2()
fun3()
fun4()
