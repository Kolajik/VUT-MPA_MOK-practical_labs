import random
from decimal import Decimal
from math import gcd

import numpy as np
import sympy
from numpy.polynomial import Polynomial as P


def randPoly(deg, mod, secret):
    coef_poly = np.random.randint(low=-mod, high=mod, size=deg)
    coef_poly = np.append(coef_poly, secret)
    coef_poly = coef_poly % mod
    p1 = P(coef_poly)
    print("Created polynomial: {}".format(p1.coef))
    return p1


def genShares(p, n, mod):
    print("\n... Generating shares ...\n")
    shares = []
    for i in range(0, n):
        x = np.random.randint(low=-mod, high=mod, size=1)
        y = np.polyval(p.coef, x) % mod
        shares.append([x[0] % mod, int(y[0]) % mod])
    print("Shares generated: {}".format(shares))
    return shares


def solveEquations(shares, deg, t, mod):
    print("\n... Solving the polynomial equations ...\n")
    coefficients = []
    results = []
    for i in range(0, t):
        tmp = []
        results.append(shares[i][1])
        for j in range(deg, 0, -1):
            x = shares[i][0] ** j % mod
            tmp.append(x)
        tmp.append(1)
        coefficients.append(tmp)
    A = sympy.Matrix(coefficients)
    print("Equations: {}".format(A))
    B = sympy.Matrix(results)
    print("Results of equations: {}".format(B))

    det = int(A.det())
    if gcd(det, mod) == 1:
        ans = pow(det, -1, mod) * A.adjugate() @ B % mod
        print("Result by finding the polynomial coefficients: {}".format(ans))
    else:
        print("Do not know the answer.")


def findInverse(x, mod):
    if gcd(x, mod) != 1:
        raise Exception("{} does not have an inverse in multiplicative group of {}".format(x, mod))
    for i in range(1, mod):
        if x * i % mod == 1:
            return i


def solveInterpolation(shares, t, mod):
    print("\n... Solving by interpolation ...\n")
    summary = 0
    for j in range(0, t):
        product = 1
        for m in range(0, t):
            if m != j:
                product = product * (shares[m][0] * findInverse((shares[m][0] - shares[j][0] % mod), mod)) % mod
        summary = (summary + (shares[j][1] * product)) % mod

    print("Secret found through interpolation: {}".format(summary % mod))
    exit(0)


if __name__ == '__main__':
    mod = 19
    n = 20
    t = 3
    degree = t - 1
    secret = 12 % mod

    p = randPoly(degree, mod, secret)
    shares = genShares(p, n, mod)

    solveEquations(shares=random.sample(shares, t), deg=degree, t=t, mod=mod)

    solveInterpolation(random.sample(shares, t), t, mod)
