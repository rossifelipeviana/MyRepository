#
#
#
import os
import sys
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from kdecorator import kdecorator


@kdecorator.timeit
def method1():
    a = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    b = pd.Series([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    c = a.reset_index(drop=True) - b.reset_index(drop=True)
    return


@kdecorator.timeit
def method2():
    a = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    b = pd.Series([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    c = a - b.values
    return


@kdecorator.timeit
def method3():
    a = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    b = pd.Series([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    c = pd.DataFrame(a.values - b.values, a.index, ['x1-x2'])
    return


@kdecorator.timeit
def method4():
    a = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    b = pd.Series([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    c = a.reset_index(drop=True) - b.reset_index(drop=True)
    return


method1()

method2()

method3()

method4()
