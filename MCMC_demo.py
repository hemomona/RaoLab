# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : MCMC_demo.py
# Time       ：2022/10/23 19:12
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""

import random
import numpy as np
from matplotlib import pylab as plt
import scipy.special as ss
plt.rcParams['figure.figsize'] = (17.0, 4.0)

# Let‘s define our Beta Function to generate s for any particular state.
# We don't care for the normalizing constant here.


# beta distribution pdf
def beta_s(w, a, b):
    return w ** (a - 1) * (1 - w) ** (b - 1)


def random_coin(p):
    unif = random.uniform(0, 1)
    if unif >= p:
        return False
    else:
        return True


# This Function runs the MCMC chain for Beta Distribution.
def beta_mcmc(N_hops, a, b):
    states = []
    cur = random.uniform(0, 1)
    for i in range(0, N_hops):
        states.append(cur)
        next = random.uniform(0, 1)
        # 没有基于模型的概率筛选，就是均匀采样
        ap = min(beta_s(next, a, b) / beta_s(cur, a, b), 1)  # Calculate the acceptance probability
        if random_coin(ap):
            cur = next
    return states[-1000:]  # Returns the last 1000 states of the chain


# Actual Beta PDF.
def beta(a, b, i):
    e1 = ss.gamma(a + b)
    e2 = ss.gamma(a)
    e3 = ss.gamma(b)
    e4 = i ** (a - 1)
    e5 = (1 - i) ** (b - 1)
    return (e1 / (e2 * e3)) * e4 * e5


# Create a function to plot Actual Beta PDF with the Beta Sampled from MCMC Chain.
def plot_beta(a, b):
    Ly = []
    Lx = []
    i_list = np.mgrid[0:1:100j]
    for i in i_list:
        Lx.append(i)
        Ly.append(beta(a, b, i))
    plt.plot(Lx, Ly, label="Real Distribution: a=" + str(a) + ", b=" + str(b))
    plt.hist(beta_mcmc(100000, a, b), density=True, bins=25,
             histtype='step', label="Simulated_MCMC: a=" + str(a) + ", b=" + str(b))
    plt.legend()
    plt.show()


plot_beta(2, 3)
