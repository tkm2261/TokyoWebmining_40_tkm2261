#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import numpy
PRODUCT_A_USE_A = 12.
PRODUCT_B_USE_A = 8.
LIMIT_USE_A = 450.
PRODUCT_A_USE_B = 3.
PRODUCT_B_USE_B = 6.
LIMIT_USE_B = 220.
PRODUCT_A_USE_C = 10.
PRODUCT_B_USE_C = 10.
LIMIT_USE_C = 420.

PRODUCT_A_PROFIT = 9.
PRODUCT_B_PROFIT = 7.

OPTIMAL_VALUE = 351.
OPTIMAL_PRODUCT_A = 28.5
OPTIMAL_PRODUCT_B = 13.5

if __name__ == "__main__":

    x = numpy.arange(0, 60, 0.01)
    y1 = [- PRODUCT_A_USE_A / PRODUCT_B_USE_A * xx
             + LIMIT_USE_A / PRODUCT_B_USE_A for xx in x]
    y2 = [- PRODUCT_A_USE_B / PRODUCT_B_USE_B * xx
             + LIMIT_USE_B / PRODUCT_B_USE_B for xx in x]
    y3 = [- PRODUCT_A_USE_C / PRODUCT_B_USE_C * xx
             + LIMIT_USE_C / PRODUCT_B_USE_C for xx in x]
    
    y4 = [- PRODUCT_A_PROFIT/PRODUCT_B_PROFIT*xx
           + OPTIMAL_VALUE/PRODUCT_B_PROFIT for xx in x]

    plt.plot(x, y1, "--", label=u"material-A limit")
    plt.plot(x, y2, "--", label=u"material-B limit")
    plt.plot(x, y3, "--", label=u"material-C limit")
    plt.plot(x, y4, "-", label="objective slope", linewidth=2)

    fill_x = [0]
    fill_y = [0]
    for i in xrange(len(x)):
        fill_x.append(x[i])
        fill_y.append(min([y1[i], y2[i], y3[i]]))

    plt.fill(fill_x, fill_y, alpha=0.2,
                label="feasible area")


    plt.plot(OPTIMAL_PRODUCT_A, OPTIMAL_PRODUCT_B, 
                'r*', label="optimal (%s, %s)"%(OPTIMAL_PRODUCT_A, OPTIMAL_PRODUCT_B), markersize=20)
    plt.legend(loc = 'upper right')
    plt.xlim([0,60])
    plt.ylim([0,90])

    plt.show()
