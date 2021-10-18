import inputs as inp
import phe
import json


# Caesar cipher
def shiftMessage(message, key):
    result = ""
    for char in message:
        resInt = int((ord(char.lower()) + key - ord('a')) % 26 + ord('a'))
        result += chr(resInt)
    return result.upper()


def sumTwoStrings(str1, str2):
    if len(str1) != len(str2):
        "No can do, sorry. String lenghts are not equal"

    result = ""
    i = 0
    for char in str1:
        resInt = int((ord(char.lower()) + ord(str2[i].lower()) - ord('a')) % 26 + ord('a'))
        result += chr(resInt)
        i += 1
    return result.upper()


def example1():
    m1 = "MPA"
    m2 = "MOK"
    key = 3

    c1 = shiftMessage(m1, key)
    c2 = shiftMessage(m2, key)
    print("m1 = {}\nc1 = {}\nm2 = {}\nc2 = {}\n".format(m1, c1, m2, c2))

    dec1 = shiftMessage(c1, -key)
    dec2 = shiftMessage(c2, -key)
    print("Dec(c1) = {}\nDec(c2) = {}\n".format(dec1, dec2))

    c3 = sumTwoStrings(c1, c2)
    dec3 = shiftMessage(c3, -2 * key)
    c1pc2 = sumTwoStrings(dec1, dec2)
    print("c3 = {}\nDec(c3) = {} == Dec(c1) + Dec(c2) = {}".format(c3, dec3, c1pc2))


def rsa_encrypt(message, pubKey, n):
    return pow(message, pubKey) % n


def rsa_decrypt(ciphertext, privKey, n):
    return pow(ciphertext, privKey) % n


def example2():
    m1 = inp.RSA_m1_2
    m2 = inp.RSA_m2_2
    n = inp.RSA_r * inp.RSA_s
    c1 = rsa_encrypt(m1, inp.RSA_pk, n)
    c2 = rsa_encrypt(m2, inp.RSA_pk, n)
    d1 = rsa_decrypt(c1, inp.RSA_sk, n)
    d2 = rsa_decrypt(c2, inp.RSA_sk, n)
    print("m1 = {}\nc1 = {}\nd1 = {}\nm2 = {}\nc2 = {}\nd2 = {}\n".format(m1, c1, d1, m2, c2, d2))

    c3 = c1 * c2 % n
    d3 = rsa_decrypt(c3, inp.RSA_sk, n)
    c1mc2 = d1 * d2 % n
    print("c3 = {}\nDec(c3, sk) = {} == Dec(c1, sk) * Dec(c2, sk) = {}".format(c3, d3, c1mc2))


def example3():
    pub_key, priv_key = phe.generate_paillier_keypair()
    n = pub_key.n
    c1 = pub_key.encrypt(inp.RSA_m1_1)
    c2 = pub_key.encrypt(inp.RSA_m1_2)

    d1 = priv_key.decrypt(c1)
    d2 = priv_key.decrypt(c2)
    print("c1 = {}\nc2 = {}\nd1 = {}\nd2 = {}".format(str(c1.ciphertext())[:20], str(c2.ciphertext())[:20], d1, d2))

    m1pm2 = (inp.RSA_m1_1 + inp.RSA_m1_2) % n
    m1mm2 = (inp.RSA_m1_1 * inp.RSA_m1_2) % n
    # Dec(c1 * c2 mod n^2) = m1 + m2 mod n
    c1mc1 = (c1.ciphertext() * c2.ciphertext()) % pow(n, 2)
    phEcryptedNumber = phe.EncryptedNumber(pub_key, c1mc1, 0)
    dec1 = priv_key.decrypt(phEcryptedNumber)
    print("Dec(c1 * c2 mod n^2) = {} == m1 + m2 mod n = {}".format(dec1, m1pm2))

    # Dec(c1 * g^m2 mod n^2) = m1 + m2 mod n
    c1mg2 = (c1.ciphertext() * pow(pub_key.g, inp.RSA_m1_2)) % pow(n, 2)
    phEcryptedNumber1 = phe.EncryptedNumber(pub_key, c1mg2, 0)
    dec2 = priv_key.decrypt(phEcryptedNumber1)
    print("Dec(c1 * g^m2 mod n^2) = {} == m1 + m2 mod n = {}".format(dec2, m1pm2))

    # Dec(c1^{m2} mod n^2) = m1 * m2 mod n
    c1m2 = pow(c1.ciphertext(), inp.RSA_m1_2) % pow(n, 2)
    phEcryptedNumber2 = phe.EncryptedNumber(pub_key, c1m2, 0)
    dec3 = priv_key.decrypt(phEcryptedNumber2)
    print("Dec(c1^m2 mod n^2) = {} == m1 * m2 mod n = {}".format(dec3, m1mm2))

    # Dec(c2^{m1} mod n^2) = m1 * m2 mod n
    c2m1 = pow(c2.ciphertext(), inp.RSA_m1_1) % pow(n, 2)
    phEcryptedNumber3 = phe.EncryptedNumber(pub_key, c2m1, 0)
    dec4 = priv_key.decrypt(phEcryptedNumber3)
    print("Dec(c2^m1 mod n^2) = {} == m1 * m2 mod n = {}".format(dec4, m1mm2))


if __name__ == '__main__':
    # example1()

    # example2()

    example3()
