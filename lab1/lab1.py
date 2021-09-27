import numpy as np


def listVsArrays():
    # Lists vs arrays
    list = [0, 1, 2, 3, 4, 5]
    vector = np.array(list)

    mod_vect = vector % 3  # Modulo is applied to each element of the list
    print("{} is a modularized list from vector.".format(mod_vect))
    n = 3
    print("{} is {}-th element from the modulrized vector".format(mod_vect[n], n))


if __name__ == '__main__':
    listVsArrays()
    pass
