import numpy as np
from numpy.polynomial import Polynomial as P
import sympy
from math import gcd


def randPoly(deg, mod, secret):
    coef_poly = np.random.randint(low=-mod, high=mod, size=deg)
    # coef_poly[deg-1] = secret
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
    print("\n... Solving the equations ...\n")
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
    # print("coefficients: {}\nresults: {}".format(coefficients, results))
    A = sympy.Matrix(coefficients)
    print("Equations: {}".format(A))
    B = sympy.Matrix(results)
    print("Results of equations: {}".format(B))

    det = int(A.det())
    if gcd(det, mod) == 1:
        ans = pow(det, -1, mod) * A.adjugate() @ B % mod
        print(ans)
    else:
        print("Do not know the answer.")


if __name__ == '__main__':
    mod = 19
    n = 4
    t = 3
    degree = t-1
    secret = 17 % mod

    p = randPoly(degree, mod, secret)
    shares = genShares(p, n, mod)
    solveEquations(shares=shares, deg=degree, t=t, mod=mod)