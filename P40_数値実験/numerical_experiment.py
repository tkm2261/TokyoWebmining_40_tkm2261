#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import numpy
from scipy.optimize import minimize, OptimizeResult
from opt_func import *
import matplotlib.pyplot as plt


numpy.random.seed(1)


def gradf(x, *args):
    A, b = args
    return numpy.dot(A, x) - b

def obj_func(x, *args):
    A, b = args
    return 0.5 * numpy.inner(x, numpy.dot(A, x)) - numpy.inner(b, x)

def print_result(result, t, args):
    try:
        print "time:", time.time() - t, "obj:", result.fun#, result.nit
    except:
        pass


def show_path():
    N = 2
    A = numpy.random.random((N, N))
    A = numpy.dot(A, A.T) + numpy.eye(N) * 0.1 #: 若干悪条件
    b = numpy.random.random(N)
    args = (A, b)
    print u"正解",
    t = time.time()
    x_correct = numpy.linalg.solve(A, b)
    print x_correct
    x0 = [1.4, 4]


    x1 = numpy.arange(-1.1, 2, 0.1)
    x2 = numpy.arange(-2, 5, 0.1)
    X1, X2 = numpy.meshgrid(x1, x2)

    Z = [[obj_func([X1[i, j], X2[i, j]], *args) for j in xrange(X1.shape[1])]
                                 for i in xrange(X1.shape[0])]

    CS = plt.contour(X1, X2, Z, 100)
    #plt.clabel(CS, inline=1, fontsize=10)


    def _callback(x):
        data.append(x)

    data = [x0]
    steepest_decent(obj_func, x0, gradf, args,
                               maxiter=1000, callback=_callback)
    data = numpy.array(data)
    plt.plot(data[:, 0], data[:, 1], marker=".",
             label=u'最急降下法({}反復)'.format(data.shape[0] - 1))

    data = [x0]
    newton_method(obj_func, x0, gradf, args,
                           maxiter=1000, callback=_callback)
    data = numpy.array(data)
    plt.plot(data[:, 0], data[:, 1], marker=".", color="r",
             label=u'ニュートン法({}反復)'.format(data.shape[0] - 1))

    data = [x0]
    minimize(obj_func, x0,method="CG", jac=gradf, args=args,
                  callback=_callback)
    data = numpy.array(data)
    plt.plot(data[:, 0], data[:, 1], marker=".", color="y",
             label=u'共役勾配法({}反復)'.format(data.shape[0] - 1))


    data = [x0]
    minimize(obj_func, x0,method="Nelder-Mead", args=args,
                  callback=_callback)
    data = numpy.array(data)
    plt.plot(data[:, 0], data[:, 1], marker=".", color="g",
             label=u"シンプレックス法({}反復)".format(data.shape[0] - 1))

    plt.legend(loc='lower left')
    plt.show()


def print_all():
    N = 2
    A = numpy.random.random((N, N))
    A = numpy.dot(A, A.T)#: 若干悪条件
    b = numpy.random.random(N)
    args = (A, b)

    t = time.time()
    x0 = numpy.zeros(N)


    print u"正解",
    x_correct = numpy.linalg.solve(A, b)
    print "time:", time.time() - t, "obj:", obj_func(x_correct, *args)

    print u"最急降下法",
    t = time.time()
    steepest = steepest_decent(obj_func, x0, gradf, args,
                               maxiter=1000)
    print_result(steepest, t, args)

    print u"ニュートン法",
    t = time.time()
    newton = newton_method(obj_func, x0, gradf, args,
                           maxiter=1000)
    print_result(newton, t, args)

    print u"共役勾配法",
    t = time.time()
    cg = minimize(obj_func, x0,method="CG", jac=gradf, args=args)
    print_result(cg, t, args)


    print u"シンプレックス法",
    t = time.time()
    cg = minimize(obj_func, x0,method="Nelder-Mead", args=args)
    print_result(cg, t, args)

if __name__ == "__main__":
    show_path()    