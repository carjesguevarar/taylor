import math


def f(n, x):
    """
    Función que devuelve el valor de la función en una de sus derivadas, o en la función original.
    :param n: Indicador del número de derivada que se desea, o cero para la función original.
    :param x: Punto en donde se evalua la función.
    :return: Valor de la función evaluada.
    """
    return {
        0: x*math.log(x),
        1: math.log(x) + 1,
        2: 1/x,
        3: -1/x**2
    }[n]


def taylor(val, n, valt):
    """
    Función que aproxiama en un punto una función dada, mediante el método de Taylor.
    :param val: Punto a aproximar en el polinomio de Taylor.
    :param n: Grado del polinomio de Taylor.
    :param valt: Valor a evaluar en el polinomio de Taylor.
    :return: Valor numérico de la evaluación en el polinomio de Taylor.
    """
    p = 0
    for i in range(n + 1):
        p = p + (f(i, val)*(valt - val)**i)/math.factorial(i)
    return p


def relerr(vn, vl):
    """
    Función que calcula el error relativo.
    :param vn: Valor actual.
    :param vl: Valor anterior.
    :return: Error relativo en base a los dos valores.
    """
    return abs((vn-vl)/vn)
