#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pulp import *
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


if __name__ == "__main__":
    # STEP1： モデルの生成
    model = LpProblem("production_plannning", LpMaximize)
    # STEP2： 変数の生成
    var_product_a_amount = LpVariable("product_a_amount",
                                      lowBound=0,
                                      upBound=None,
                                      cat=LpContinuous)
     
    var_product_b_amount = LpVariable("product_b_amount",
                                      lowBound=0,
                                      upBound=None,
                                      cat=LpContinuous)
     
    # STEP3： 制約の追加
    model += (PRODUCT_A_USE_A * var_product_a_amount
              + PRODUCT_B_USE_A * var_product_b_amount <= LIMIT_USE_A,
              'coal supply constraint')
    model += (PRODUCT_A_USE_B * var_product_a_amount
              + PRODUCT_B_USE_B * var_product_b_amount <= LIMIT_USE_B,
              'electric-power supply constraint')
    model += (PRODUCT_A_USE_C * var_product_a_amount
              + PRODUCT_B_USE_C * var_product_b_amount <= LIMIT_USE_C,
              'man-power supply constraint')
    # STEP4： 目的変数の追加
    model += PRODUCT_A_PROFIT * var_product_a_amount \
             + PRODUCT_B_PROFIT * var_product_b_amount
     
    # STEP5： パラメータ（ソルバー）の設定および、最適化の実行
    solver = COIN_CMD(maxSeconds=3600, threads=4)
    model.solve(solver)
    model.writeLP("aaa.lp")
    # STEP6： 解の取得
    print "status: ", LpStatus[model.status]
    print "profit: ", model.objective.value()
    print "product A amount :", var_product_a_amount.value()
    print "product B amount :", var_product_b_amount.value()
