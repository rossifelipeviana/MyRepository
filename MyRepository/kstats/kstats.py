###############################################################################
# Some automations for some statistical treatments.
# Focus on RDC 166 - Validação de Métodos Analíticos.
# Some functions translated to my needs and elucidations (PT-BR).
###############################################################################

import pandas as pd
import numpy as np
from scipy import stats
from ..kdecorator.kdecorator import *


@do_have_1d
def isweight(weight):
    try:
        if weight == None:
            weight = list()
            for n in range(len(weight)):
                weight.append(1)
    except:
        pass


@do_have_1d
def somatorio(*args):
    # Não feito
    valores = args
    s = 0
    for n in valores:
        s += n
    return s


def somadoquadradodasdiferencas():
    # TODO
    pass
    return


@do_have_1d
def media_aritimetica(*args):
    # (GUM2018, p. 10, eq. 3.)
    valores = args
    m = 0
    n = len(valores)
    for i in valores:
        m += i
    m = m / n
    return m


@do_have_1d
def mediaharmonica(*args):
    valores = args
    denominador = 0
    for i in valores:
        denominador += 1 / i
    mediah = len(valores) / denominador
    return mediah


@do_have_1d
def variancia_experimental(*args):
    # (GUM2018 p.10, eq. 4)
    valores = args
    n = len(valores)
    mean = media_aritimetica(valores)
    ve = 0
    for i in valores:
        ve += (i - mean) ** 2
    ve = ve / (n - i)
    return ve


@do_have_1d
def variancia_experimental_media(*args):
    # (GUM2018, p. 10, eq. 5)
    valores = args
    n = len(valores)
    vem = variancia_experimental(valores) / n
    return vem


def SQTot(y, weight=None):
    try:
        if weight == None:
            weight = list()
            for n in range(len(y)):
                weight.append(1)
    except:
        pass
    if do_have_1d(y):
        y = do_have_1d(y)
    y_mean = media_aritimetica(y)
    SQTot = 0
    for n in range(len(y)):
        SQTot += weight[n] * (y[n] - y_mean) ** 2
    return SQTot


def SQReg(y, predict, weight=None):
    try:
        if weight == None:
            weight = list()
            for n in range(len(y)):
                weight.append(1)
    except:
        pass
    if do_have_1d(y) and do_have_1d(predict):
        y = do_have_1d(y)
        yp = do_have_1d(predict)
    y_mean = media_aritimetica(y)
    if len(y) == len(yp):
        SQReg = 0
        for n in range(len(y)):
            SQReg += weight[n] * (yp[n] - y_mean) ** 2
        return SQReg


def SQRes(y, predict, weight=None):
    try:
        if weight == None:
            weight = list()
            for n in range(len(y)):
                weight.append(1)
    except:
        pass
    if do_have_1d(y) and do_have_1d(predict):
        y = do_have_1d(y)
        yp = do_have_1d(predict)
    if len(y) == len(yp):
        SQReg = 0
        for n in range(len(y)):
            SQReg += weight[n] * (yp[n] - y[n]) ** 2
        return SQReg


def QMTot(y, weight=None):
    try:
        if weight == None:
            weight = list()
            for n in range(len(y)):
                weight.append(1)
    except:
        pass
    QMTot = SQTot(y, weight) / (len(y) - 1)
    return QMTot


def QMReg(y, predict, weight=None):
    try:
        if weight == None:
            weight = list()
            for n in range(len(y)):
                weight.append(1)
    except:
        pass
    QMReg = SQReg(y, predict, weight) / (2 - 1)
    return QMReg


def QMRes(y, predict, weight=None):
    try:
        if weight == None:
            weight = list()
            for n in range(len(y)):
                weight.append(1)
    except:
        pass
    QMRes = SQRes(y, predict, weight) / (len(y) - 2)
    return QMRes


def ANOVA(y, replicatas, predict, weight=None):
    try:
        if weight == None:
            weight = list()
            for n in range(len(y)):
                weight.append(1)
    except:
        pass
    n = len(y) * replicatas
    p = len(y)
    F = QMReg(y, predict, weight) / QMRes(y, predict, weight)
    p = stats.f.cdf(QMReg / QMRes, p - 1, n - p)
    return F, p


@do_have_1d
def cochran(*args):
    lista = args
    var_max = 0
    var_sum = 0
    for n in lista:
        if n > var_max:
            var_max = n
        var_sum += n
    cochran = var_max / var_sum
    stats.f.cdf()
