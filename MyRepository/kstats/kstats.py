###############################################################################
# Some automations for some statistical treatments.
# Focus on RDC 166 - Validação de Métodos Analíticos.
# Some functions translated to my needs and elucidations (PT-BR).
###############################################################################

from scipy import stats

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from functools import cache
from kdecorator import kdecorator


@kdecorator.do_have_1d
def isweight(weight):
    if weight is None:
        weight = 1 #CHECKME


@kdecorator.do_have_1d
def somatorio(*args):
    # Não feito
    valores = args
    s = 0
    for valor in valores:
        s += valor
    return s


def somadoquadradodasdiferencas():
    # TODO
    return


@kdecorator.do_have_1d
def media_aritimetica(*args):
    # (GUM2018, p. 10, eq. 3.)
    valores = args
    m = 0
    n = len(valores)
    for valor in valores:
        m += valor
    m = m / n
    return m


@kdecorator.do_have_1d
def mediaharmonica(*args):
    valores = args
    denominador = 0
    for valor in valores:
        denominador += 1 / valor
    mediah = len(valores) / denominador
    return mediah


@kdecorator.do_have_1d
def variancia_experimental(*args):
    # (GUM2018 p.10, eq. 4)
    valores = args
    n = len(valores)
    mean = media_aritimetica(valores)
    ve = 0
    for valor in valores:
        ve += (valor - mean) ** 2
    ve = ve / (n - 1)  # FIXME:
    return ve


@kdecorator.do_have_1d
def variancia_experimental_media(*args):
    # (GUM2018, p. 10, eq. 5)
    valores = args
    n = len(valores)
    vem = variancia_experimental(valores) / n
    return vem


# @kdecorator.lru_cache
def SQTot(y, weight=None):
    if weight is None:
        weight = [1] * len(y)
    if kdecorator.do_have_1d(y):
        ys = kdecorator.do_have_1d(y)
    y_mean = media_aritimetica(y)
    SQTot = 0
    for index, y in enumerate(ys):
        SQTot += weight[index] * (ys[index] - y_mean) ** 2
    return SQTot


# @kdecorator.lru_cache
def SQReg(y, predict, weight=None):
    if weight is None:
        weight = [1] * len(y)
    if kdecorator.do_have_1d(y) and kdecorator.do_have_1d(predict):
        ys = kdecorator.do_have_1d(y)
        yps = kdecorator.do_have_1d(predict)
    y_mean = media_aritimetica(ys)
    if len(ys) == len(yps):  # assert
        SQReg = 0
        for index, ys in enumerate(ys):
            SQReg += weight[index] * (yps[index] - y_mean) ** 2
        return SQReg
    return print('Algo de errado aconteceu')  # FIXME:


# @kdecorator.lru_cache
def SQRes(y, predict, weight=None):
    if weight is None:
        weight = [1] * len(y)
    if kdecorator.do_have_1d(y) and kdecorator.do_have_1d(predict):
        ys = kdecorator.do_have_1d(y)
        yps = kdecorator.do_have_1d(predict)
    if len(ys) == len(yps):
        SQReg = 0
        for index, y in enumerate(ys):
            SQReg += weight[index] * (yps[index] - ys[index]) ** 2
        return SQReg
    return print('Algo de errado aconteceu')  # FIXME:


# @kdecorator.lru_cache
def QMTot(y, weight=None):
    if weight is None:
        weight = [1] * len(y)
    QMTot = SQTot(y, weight) / (len(y) - 1)
    return QMTot


# @kdecorator.lru_cache
def QMReg(y, predict, weight=None):
    if weight is None:
        weight = [1] * len(y)
    QMReg = SQReg(y, predict, weight) / (2 - 1)
    return QMReg


# @kdecorator.lru_cache
def QMRes(y, predict, weight=None):
    if weight is None:
        weight = [1] * len(y)
    QMRes = SQRes(y, predict, weight) / (len(y) - 2)
    return QMRes


def ANOVA(y, replicatas, predict, weight=None):
    if weight is None:
        weight = [1] * len(y)
    n = len(y) * replicatas
    p = len(y)
    F = QMReg(y, predict, weight) / QMRes(y, predict, weight)
    p = stats.f.cdf(QMReg / QMRes, p - 1, n - p)
    return F, p


@kdecorator.do_have_1d
def cochran(*args):
    lista = args
    var_max = 0
    var_sum = 0
    for n in lista:
        if n > var_max:
            var_max = n
        var_sum += n
    cochran = var_max / var_sum
    stats.f.cdf(lista)  # CHECKME:
    return cochran
