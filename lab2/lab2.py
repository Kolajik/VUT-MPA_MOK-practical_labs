import numpy as np
import lib.lattice as lt


def listVsArrays(number):
    # Lists vs arrays
    list = [0, 1, 2, 3, 4, 5]
    vector = np.array(list)

    mod_vect = vector % 3  # Modulo is applied to each element of the list
    print("{} is a modularized list from vector.".format(mod_vect))
    if not number > len(list):
        print("{} is {}-th element from the modulrized vector".format(mod_vect[number], number))
    else:
        print("Number provided too big.")


def exampleOne(seed, dim, mod):
    np.random.seed(seed)
    v = np.random.randint(low=-(mod - 1), high=mod - 1, size=dim)
    print("Generated vector:\n{}".format(v))
    m = np.random.randint(low=-(mod - 1), high=mod - 1, size=(dim, dim))
    print("Generated matrix:\n{}".format(m))

    return m.dot(v) % mod


def goodOrBadBasis():
    list = [[2, 0, 0], [1, 1, 0], [0, 0, 3]]
    l = np.array(list)
    print("Good matrix:\n{}\n".format(l))
    print("Hadamard ratio of L: {}\n".format(lt.hamdamard_ratio(l)))
    u = lt.rand_unimod(3, 3)
    print("Uniform matrix:\n{}\n".format(u))
    b = np.matmul(l, u)
    print("Bad matrix:\n{}\n".format(b))

    print("Hadamard ratio of B: {}".format(lt.hamdamard_ratio(b)))


def distance_LatticeVector(basis, vector):
    b = lt.babai(basis, vector)
    print("Babai point: {}".format(b))
    distance = np.linalg.norm(np.abs(v2 - b))

    return distance


def compareDistances(basis1, basis2, vector):
    basis1Dist = distance_LatticeVector(basis1, vector)
    basis2Dist = distance_LatticeVector(basis2, vector)

    if basis1Dist > basis2Dist:
        print("Basis 1 ({}) is higher than Basis 2 ({})".format(basis1Dist, basis2Dist))
    elif basis2Dist > basis1Dist:
        print("Basis 2 ({}) is higher than Basis 1 ({})".format(basis2Dist, basis1Dist))
    else:
        print("Both distances are equal ({}).".format(basis1Dist))


if __name__ == '__main__':
    # listVsArrays(9)

    # print("M*v = \n{}".format(exampleOne(3, 3, 10)))

    # goodOrBadBasis()

    basis1 = np.array([[2, 0, 0], [1, 1, 0], [0, 0, 3]])
    basis2 = np.array([[98, -22, -4], [-4, 1, 0], [-10, 2, 1]])
    v1 = np.array([-5, 1, 0])
    v2 = np.array([-10, 1, 13])
    print(distance_LatticeVector(basis1, v2))

    compareDistances(basis2, basis1, v1)
