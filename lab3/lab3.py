import numpy as np
from numpy.polynomial import polynomial as poly
from numpy.polynomial import Polynomial as P

# Trying out polynomials


def learningPolynomials():
    p1 = P([1, 2, 3])
    print("p1 = ", p1)

    p = P([2, 1, 3])
    print("p = ", p)

    print("p1 coefficients = ", p1.coef)

    coef_poly = np.random.randint(low=-10, high=10, size=3)
    p1 = P(coef_poly)
    print("p1 randomized = ", p1)


def computationOnPolys():
    coef_poly = np.random.randint(low=-10, high=10, size=3)
    p1 = P(coef_poly)
    print("p1 randomized = ", p1.coef)

    # Addition on polynomials
    p2 = P(poly.polyadd(p1.coef, p1.coef))
    print("p2 = p1 + p1 = ", p2.coef)

    # Subtraction on polynomials
    p3 = P(poly.polysub(p2.coef, p1.coef))
    print("p3 = p2 - p1 = ", p3.coef)

    # Polynomial multiplication
    p4 = P(poly.polymul(p1.coef, p1.coef))
    print("p4 = p1 * p1 = ", p4.coef)

    # Polynomial division
    p5 = P(poly.polydiv(p4.coef, p1.coef))
    print("p5 = p4 / p1 = ", p5.coef)


def example1(mod, seed):
    print("\n\tEXAMPLE 1: polyadd_mod function \n")
    r = P([1, 0, 1])
    print("r = ", r.coef)

    np.random.seed(seed)
    p1 = P(np.random.randint(low=-mod, high=mod, size=5))
    p2 = P(np.random.randint(low=-mod, high=mod, size=5))

    print("p1 = {}\np2 = {}".format(p1.coef, p2.coef))

    print("polyadd_mod(p1, p2, 11, r) =", polyadd_mod(p1, p2, 11, r))
    print("polyadd_mod(p1, p2, 5, r) =", polyadd_mod(p1, p2, 5, r))


def polyadd_mod(y, z, mod, poly_mod):
    polyadd = P(poly.polyadd(y.coef, z.coef) % mod)
    # print("polyadd = ", polyadd)
    return poly.polydiv(polyadd.coef, poly_mod.coef)


def example2(mod, seed):
    print("\n\tEXAMPLE 2: polymul_mod function \n")
    r = P([1, 0, 1])
    print("r = ", r.coef)

    np.random.seed(seed)
    p1 = P(np.random.randint(low=-mod, high=mod, size=5))
    p2 = P(np.random.randint(low=-mod, high=mod, size=5))

    print("polymul_mod(p1, p2, 11, r) =", polymul_mod(p1, p2, 11, r))
    print("polymul_mod(p1, p2, 5, r) =", polymul_mod(p1, p2, 5, r))


def polymul_mod(y, z, mod, poly_mod):
    polymul = P(poly.polymul(y.coef, z.coef) % mod)
    # print("polymul = ", polymul)
    return poly.polydiv(polymul.coef, poly_mod.coef)


def example3():
    print("\n\tEXAMPLE 3: R-LWE Keygen \n")
    poly_mod = P([1, 0, 1])
    print("poly_mod = ", poly_mod.coef)
    (a, b), s = keygen(2, 4, 5, poly_mod)


def keygen(seed, dim, mod, poly_mod):
    np.random.seed(seed)
    a = P(np.random.randint(low=-mod, high=mod, size=dim))
    e = P(np.random.normal(0, 2, size=dim))
    s = P(np.random.randint(0, 2, size=dim))

    b = P(poly.polysub(poly.polymul(-a.coef, s.coef), e.coef))
    print("a = {}\ne = {}\ns = {}\nb = {}".format(
        a.coef, e.coef, s.coef, b.coef))

    return (a, b), s


def example4():
    print("\n\tEXAMPLE 4: R-LWE Encryption/Decryption \n")
    seed = 2
    dimensions = 4
    mod = 11
    t = 7
    poly_mod = P([1, 0, 1])

    (a, b), s = keygen(seed, dimensions, mod, poly_mod)

    (ct0, ct1) = encrypt(5, (a, b), dimensions, mod, t, poly_mod, 8)
    print("ct0 = {}\nct1 = {}".format(ct0, ct1))

    decrypted_text = decrypt(s, mod, t, poly_mod, (ct0, ct1))
    print(decrypted_text)


def encrypt(seed, pk, dim, q, t, poly_mod, pt):
    np.random.seed(seed)
    u = P(np.random.randint(0, 2, size=dim))
    delta = q // t
    e1 = P(np.random.normal(0, 2, size=dim))
    e2 = P(np.random.normal(0, 2, size=dim))
    # a, b, s = keygen(seed, dim, q, poly_mod)
    m = np.random.randint(low=-q, high=q, size=dim)
    m[1:] = 0
    scaled_pt = P((delta * m) % q)

    ct0 = poly.polyadd(scaled_pt.coef, poly.polyadd(e1.coef,
                       poly.polymul(pk[0].coef, u.coef)))
    ct0 = P(ct0 % q)

    ct1 = poly.polyadd(e2.coef, poly.polymul(pk[1].coef, u.coef))
    ct1 = P(ct1 % q)

    return (ct0, ct1)


def decrypt(sk, mod, t, poly_mod, ct):
    scaled_pt = polyadd_mod(
        P(polymul_mod(ct[1], sk, mod, poly_mod)[0]), ct[0], mod, poly_mod)
    delta = mod // t
    decrypted_poly = np.round(scaled_pt[0] / delta) % t
    print("decrypted_poly = ", decrypted_poly)
    return int(decrypted_poly[0])


if __name__ == '__main__':
    # learningPolynomials()

    # computationOnPolys()

    # example1(7, 666)

    # example2(7, 666)

    # I am really not sure why poly_mod variable is needed in these examples below...
    # example3()

    example4()
