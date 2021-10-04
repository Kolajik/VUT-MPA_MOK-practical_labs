"""
Example 3 / Homework 1 implementation
author: David Kolaja
"""

import libraries.ggh_plain as ggh
import numpy as np

if __name__ == '__main__':
    messageA = "Hey what's up, Bob?"

    #KeyGeneration Alice
    dimensionA = 4
    privateKeyA, publicKeyA, badVectorA = ggh.keyGeneration(dimensionA)

    print("Alice's private key:\n {}\n"
          "Alice's public key:\n {}".format(privateKeyA, publicKeyA))
    print("Hadamard ratio of Alice's private key: {}".format(ggh.hamdamard_ratio(privateKeyA, dimensionA)))
    print("Hadamard ratio of Alice's public key: {}\n".format(ggh.hamdamard_ratio(publicKeyA, dimensionA)))

    # Unimodular matrix from dimensions
    unimodA = ggh.rand_unimod(dimensionA)
    print("Unimodular matrix from Alice's lattice dimensions: \n{}".format(unimodA))

    # Encryption on Bob's side
    rndOpenTxtB = np.random.randint(low=-(dimensionA - 1), high=dimensionA - 1, size=dimensionA)
    while len(str(rndOpenTxtB)) != 4:
        rndOpenTxtB = np.random.randint(low=0000, high=9999)
    with open('messages/BobMessage.txt', 'w') as file:
        file.write(str(rndOpenTxtB))
    print("Bob's open message which is sent to Alice:\n {}".format(rndOpenTxtB))

    ciphertextBob = ggh.encrypt('messages/BobMessage.txt', publicKeyA)
    print("Bob's ciphertext which is sent to Alice:\n {}\n".format(ciphertextBob))

    #Decryption on Alice's side
    decryptedMsgAliceSide = ggh.decrypt(ciphertextBob, privateKeyA, publicKeyA, unimodA)
    print("Alice's decrypted message from Bob: \n{}".format(decryptedMsgAliceSide))