#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import numpy
from scipy.optimize import minimize, OptimizeResult


def steepest_decent(fun, x0, fprime, args, tol=1.0e-4, maxiter=1000,
                    callback=None):
    '''最急降下法
    '''
    x = numpy.array(x0)

    for itr in xrange(maxiter):
        direction = -1 * fprime(x, *args)
        alpha, obj_current, obj_next = armijo_stepsize(fun, x, fprime, direction, args=args)

        if numpy.linalg.norm(obj_current - obj_next) < tol:
            break

        x = x + alpha * direction
        if callback is not None:
            callback(x)

    result = OptimizeResult()
    result.x = x
    result.fun = fun(x, *args)
    result.nit = itr
    return result



def newton_method(fun, x0, fprime, args, tol=1.0e-4, maxiter=1000,
                    callback=None):
    '''ニュートン法 ステップサイズにArmijo条件
    '''
    x = numpy.array(x0)
    A, b = args

    for itr in xrange(maxiter):
        direction =  -1 * numpy.linalg.solve(A, fprime(x, *args))
        alpha, obj_current, obj_next = armijo_stepsize(fun, x, fprime, direction, args=args)

        if numpy.linalg.norm(obj_current - obj_next) < tol:
            break

        x = x + alpha * direction
        if callback is not None:
            callback(x)

    result = OptimizeResult()
    result.x = x
    result.fun = fun(x, *args)
    result.nit = itr
    return result

def armijo_stepsize(fun, x, fprime, d, args=None, alpha0=1000., tau=0.1, xi=0.5,
                    maxiter=10):
    '''Armijo条件を満たすステップサイズ決定関数
    '''
    alpha = float(alpha0)
    obj_current = fun(x, *args)
    direction_product = numpy.inner(d, fprime(x, *args))

    for i in xrange(maxiter):
        obj_next = fun(x + alpha * d, *args)
        armijo = obj_next <= obj_current + xi * alpha * direction_product
        #armijo = obj_next < obj_current
        if armijo:
            break

        alpha = alpha * tau

    else:
        alpha = 0.

    return alpha, obj_current, obj_next

