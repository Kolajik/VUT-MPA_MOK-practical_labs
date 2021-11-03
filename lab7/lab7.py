import numpy as np
from numpy.polynomial import Polynomial as P
import sympy
from math import gcd


def randPoly(deg, mod, secret):
    coef_poly = np.random.randint(low=-mod, high=mod, size=deg)
    # coef_poly[deg-1] = secret
    coef_poly = np.append(coef_poly, secret)
    p1 = P(coef_poly)
    print("Created polynomial: {}".format(p1.coef))
    return p1


def genShares(p, s, mod):
    shares = []
    for i in range(0, s):
        x = np.random.randint(low=-mod, high=mod, size=1)
        y = np.polyval(p.coef, x) % mod
        shares.append([x[0], int(y[0])])
    print("Shares generated: {}".format(shares))
    return shares


def solveEquations(shares, deg, t, mod):
    coefficients = []
    results = []
    for i in range(0, t):
        tmp = []
        results.append(shares[i][1])
        for j in range(deg, 1, -1):
            x = shares[i][0] ** j % mod
            tmp.append(x)
        tmp.append(1)
        coefficients.append(tmp)
    print("coefficients: {}\nresults: {}".format(coefficients, results))
    A = sympy.Matrix(coefficients)
    print("A: {}".format(A))
    B = sympy.Matrix(results)

    det = int(A.det())
    if gcd(det, mod) == 1:
        ans = pow(det, -1, mod) * A.adjugate() @ B % mod
        print(ans)
    else:
        print("Do not know the answer.")


if __name__ == '__main__':
    np.random.seed(665)
    mod = 17
    n = 4
    t = 3
    degree = t-1
    secret = 12

    p = randPoly(degree, mod, secret)

    testing = P([3, 14, 12])
    testingShares = [[4, 2], [2, 14], [1, 10], [3, 5]]

    shares = genShares(testing, degree, mod)
    solveEquations(shares=testingShares, deg=degree+1, t=t, mod=mod)