###############################################################################
# Some automations for some statistical treatments.
# Focus on RDC 166 - Validação de Métodos Analíticos.
# Some functions translated to my needs and elucidations (PT-BR).
###############################################################################

from scipy import stats
from ..kdecorator.kdecorator import *


@do_have_1d
def isweight(weight):
    if weight is None:
        weight = 1 #CHECKME


@do_have_1d
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


@do_have_1d
def media_aritimetica(*args):
    # (GUM2018, p. 10, eq. 3.)
    valores = args
    m = 0
    n = len(valores)
    for valor in valores:
        m += valor
    m = m / n
    return m


@do_have_1d
def mediaharmonica(*args):
    valores = args
    denominador = 0
    for valor in valores:
        denominador += 1 / valor
    mediah = len(valores) / denominador
    return mediah


@do_have_1d
def variancia_experimental(*args):
    # (GUM2018 p.10, eq. 4)
    valores = args
    n = len(valores)
    mean = media_aritimetica(valores)
    ve = 0
    for valor in valores:
        ve += (valor - mean) ** 2
    ve = ve / (n - valor)
    return ve


@do_have_1d
def variancia_experimental_media(*args):
    # (GUM2018, p. 10, eq. 5)
    valores = args
    n = len(valores)
    vem = variancia_experimental(valores) / n
    return vem


def SQTot(y, weight=None):
    if weight is None:
        weight = list[]*len(y)
    if do_have_1d(y):
        y = do_have_1d(y)
    y_mean = media_aritimetica(y)
    SQTot = 0
    for n in range(len(y)):
        SQTot += weight[n] * (y[n] - y_mean) ** 2
    return SQTot


def SQReg(y, predict, weight=None):
    if weight is None:
        weight = list[]*len(y)
    if do_have_1d(y) and do_have_1d(predict):
        y = do_have_1d(y)
        yp = do_have_1d(predict)
    y_mean = media_aritimetica(y)
    if len(y) == len(yp):
        SQReg = 0
        for n in range(len(y)):
            SQReg += weight[n] * (yp[n] - y_mean) ** 2
        return SQReg
    return print('algo deve ser veito')

def SQRes(y, predict, weight=None):
    if weight is None:
        weight = list[]*len(y)
    if do_have_1d(y) and do_have_1d(predict):
        y = do_have_1d(y)
        yp = do_have_1d(predict)
    if len(y) == len(yp):
        SQReg = 0
        for n in range(len(y)):
            SQReg += weight[n] * (yp[n] - y[n]) ** 2
        return SQReg
    return print('algo deve ser veito')

def QMTot(y, weight=None):
    if weight is None:
        weight = list[]*len(y)
    QMTot = SQTot(y, weight) / (len(y) - 1)
    return QMTot


def QMReg(y, predict, weight=None):
    if weight is None:
        weight = list[]*len(y)
    QMReg = SQReg(y, predict, weight) / (2 - 1)
    return QMReg


def QMRes(y, predict, weight=None):
    if weight is None:
        weight = list[]*len(y)
    QMRes = SQRes(y, predict, weight) / (len(y) - 2)
    return QMRes


def ANOVA(y, replicatas, predict, weight=None):
    if weight is None:
        weight = list[]*len(y)
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
    stats.f.cdf(args) #CHECKME
