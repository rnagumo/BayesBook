#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def main():



    # Parameters
    mu = np.zeros(D)
    lmd_k = np.matrix(np.zeros((D, D)))

    # Latent variable
    s_n = np.zeros(K)

    # Hyper-parameters
    # For categorical distribution
    pi = np.zeros(K)

    # For Gauss-Wishart distribution
    m = np.zeros(D)
    beta = 0
    nu = 0
    W = np.zeros((D, D))

    # Sample a GMM given hyper parameters
    mu = stats.norm.rvs(m, 1 / beta * lmd_k.I)
    lmd_k = stats.wishart.rvs(nu, W.I)


if __name__ == '__main__':
    main()
