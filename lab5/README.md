# Laboratory 5 - Homomorphic Encryption

Homomorphic encryption is a form of encryption that allows specific types of computations to be carried out on ciphertexts and generate an encrypted result that, when decrypted, matches the result of operations performed on the plaintexts.

## Ceasar cipher (100-44 BC)
* This is a simple substitution cipher (i.e.,symmetric cipher)
* If you have the key, you can encrypt and decrypt
* The default Key value is 3

---
**NOTE:** today, the cipher is completely insecure!  
Ceasar cipher is only **additively homomorphic**.

---

**Encryption** = shift right by 3 (Key value) places on the supported alphabet
![caesar_enc.png](caesar_enc.png)

**Decryption** = shift left by 3 (Key value) places on the supported alphabet
![caesar_dec.png](caesar_dec.png)

### Ex. 1 (1p)
* implement Caesar encryption and decryption function
* please use the alphabet and the key value from [inputs.py](inputs.py)
* implement a function that proves that Caesar cipher is additively homomorphic
* use the values from [inputs.py](inputs.py)
* check if the following equation holds:
   * *m1 + m2 = dec(c1, key) + dec(c2, key) = dec(c3, 2 x key)* where
      * *c1 = enc(m1,key)*
      * *c2 = enc(m2,key)*
      * *c3 = Sum(c1,c2)*

![caesar_add.png](caesar_add.png)

---
[Solution](caesar.py)

---

## RSA

![rsa_enc.png](rsa_enc.png)
![rsa_system.png](rsa_system.png)


### Ex. 2 (1p)
* implement basic RSA function for enc and dec
   * just basic computations over integers
   * *rsa_enc(message, public_key, n)*
   * *rsa_dec(cipher_text, private_key, n)*
   * both return computed value
* implement a function that proves that RSA cipher is multiplicatively homomorphic
   * use the values from [inputs.py](inputs.py)
   * check if the following equation holds:
   * *m1 x m2 = dec(c1, sk) x dec(c2, sk) = dec(c3, sk)* where
      * *c1 = enc(m1, pk)*
      * *c2 = enc(m2, pk)*
      * *c3 = enc(m1, pk) x enc(m2, pk)*

![rsa_mul.png](rsa_mul.png)

---
[Solution](rsa.py)

---

## Paillier Encryption Scheme:

* is a probabilistic public-key algorithm for asymmetric encryption,
* published in 1999, used upto now,
* based on composite residuosity assumption,
* The scheme is an additive homomorphic cryptosystem.

```console
pip3 install phe
```

```python
import phe
```

Check [Doc](https://python-paillier.readthedocs.io/en/develop/) and [Usage](https://python-paillier.readthedocs.io/en/develop/usage.html#usage), Also [useful](https://python-paillier.readthedocs.io/en/stable/phe.html).

### Ex. 3 (1p)
* implement a function that proves Paillier homomorphic properties
   * use the values from [inputs.py](inputs.py)
   * check if the following equation holds:
      * Dec(c1 * c2 mod n^2) = m1 + m2 mod n
      * Dec(c1 * g^m2 mod n^2) = m1 + m2 mod n
      * Dec(c1^{m2} mod n^2) = m1 * m2 mod n
      * Dec(c2^{m1} mod n^2) = m1 * m2 mod n

![pailler_scheme.png](pailler_scheme.png)

---
[Solution](pailler.py)

---

### Hw. 1 (1p) - Create the e-voting scheme
* Here DJN scheme (in slides g = (n+1) instead of g= (n+1)x  for simplicity). It is also called DJ scheme. Here the python3 implementation: https://github.com/cryptovoting/damgard-jurik 

![evote.png](evote.png)

