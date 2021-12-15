# Laboratory 3 - Numpy on Polynomials and R-LWE problem

NumPy has a package dedicated to polynomials: numpy.polynomial. 

We need to import the libraryies:
  ```python
  import numpy as np
  from numpy.polynomial import polynomial as poly
  from numpy.polynomial import Polynomial as P
  ```
---  
**NOTE**: P and poly are different:
* P allows defining a polynomial. Here a polynomial is represented as an equation.
* poly allows making computations on polynomials. Here a polynomial is represented as the vector of its coefficients (*array representation*).  
---

**For ipython3 users (others can skip):** 

Unluckily, *ipython3* does not allow to print polynomial in equation format by simply using *print()* command. 
Let p1 be the polynomial that you would like to print. 

In our case, the command
 ```python
 print(p1) 
 ```
depicts the coefficient of the polynomial.

You can define the following function: 
```python
def get_prettified_output(polynomial):
    prettified_output = ""
    coefficients = polynomial.coef
    for i in range(len(coefficients)):
        prettified_output+= str(coefficients[i])+"x^"+str(i)+" + "
    return prettified_output[:-2]
```
and then 
```python
print(get_prettified_output(p1))
```

## Create a polynomial

In this case, we need library P. 

A polynomial can be created from its coefficients given as an array or list. Try the command:
  ```python
  p1 = P([1,2,3])
  print(p1)
  ```
Please check the ordering of the coefficients [1,2,3] with the powers of x: 
1 + 2 x + 3 x^2

Try:
  ```python
  p = P([2,1,3])
  print(p)
  ```

Given a polynomial p1, we can extract the coefficients using: 
```python
p1.coef
print(p1.coef)
```
**Note**: a polynomial can be represented as an equation 1+2x+3x^2 or as an array [1,2,3].

Since a polynomial is generated from an array and numpy allows to generate random arrays, we can generate a polynomial at random. 
We can try to generate a polynomial of degree 3 at random in Z_11[x]: 
```python
coef_poly = np.random.randint(low=-10,high=10,size=3)
p1 = P(coef_poly)
print(p1)
```
Please check [Laboratory 2](https://github.com/xcibik00/MPA-MOK/tree/cibik_readme/labs/lab2) for more details on how to generate an array mod 11 at random. 

## Computations with polynomials

We want to add, subtract, multiply and divide polynomials. 
Library poly has defined the above operations. 

**IMPORTANT**: This library uses the array representation.  

We can 
* add polynomials
  ```python
  p2 = poly.polyadd(p1.coef,p1.coef) 
  print(p2) 
  ```
* subtract polynomials 
  ```python
  p3 = poly.polysub(p2.coef,p1.coef) 
  print(p3) 
  ```
* multiply polynomials
  ```python
  p4 = poly.polymul(p1.coef,p1.coef) 
  print(p4) 
  ```
* divide polynomials
  ```python
  p5 = poly.polydiv(p2.coef,p1.coef) 
  print(p5) 
  ```
---

**Note**: the input of the aforementioned functions is the array of coefficients, therefore:
* p1.coef: you create p1 = P([1,2,3]) and then you consider the coeffients of p1
* np.array([1,2,3]): you directly consider the coefficient "without definining the polynomial"  

---
  
The command poly.polydiv(array,array) can be used for creating the classes of polynomials in Zp[x]/(p1)

### Ex. 1
Let *mod* be the modulus and *seed* the seed of a random number generator.  
* create the polynomial *r = x^2 + 1* (array representation)
* generate 2 polynomials *p1* and *p2* (array representation) of degree 5 at random (using seed *seed*) with coefficients modulus *mod*
* create a function polyadd_mod that add two polynomials in Zp[x]/(f(x))  
* **input**: *y*, *z*, *mod*, and *poly_mod*, where 
  * y, z: two polynomials to be added.
  * mod: coefficient modulus.
  * poly_mod: polynomial modulus. 
* **output** the polynomial y+z in Z_mod[x]/(poly_mod).
* compute polyadd_mod(p1,p2,11,r) and polyadd_mod(p1,p2,5,r)
---
**Hint**: You need to divide y+z by poly_mod. 

[Solution](Ex1.py) and [Example](Ex1.png)

### Ex. 2
Let *mod* be the modulus and *seed* the seed of a random number generator.  
* create the polynomial *r = x^2 + 1* (array representation)
* generate 2 polynomials *p1* and *p2* (array representation) of degree 5 at random (using seed *seed*) with coefficients modulus *mod*
* create a function polymul_mod that multiply two polynomials in Zp[x]/(f(x))  
* **input**: *y*, *z*, *mod*, and *poly_mod*, where 
  * y, z: two polynomials to be multiplied.
  * mod: coefficient modulus.
  * poly_mod: polynomial modulus. 
* **output** the polynomial yz in Z_mod[x]/(poly_mod).
* compute polymul_mod(p1,p2,11,r) and polymul_mod(p1,p2,5,r)
---

[Solution](Ex2.py) 


## R-LWE problem generation

LWE and R-LWE problems roughly say:

*Given (A,As+e), it is hard to compute s*

---
**Note**: In LWE, we have vestors and in RLWE we have polynomials. 
However, we saw that the problmes are "two sides of the same coin", i.e., we can pass from one representation to the other. 

---

In the specification, we have that: 
1. *A* and *s* are generated at random, 
2. *e* follows the normal distribution, 

Below the Python commands.

1. We already know how to generate a random vector of integers from the uniform ditristribution.
   Let p be a random polynomial of degree 3 in Z11[x]. Therefore, A can be generated with the following command:
   ```python
   A = np.random.randint(low=-10,high=10,size=(4,4))
   ```
2. In case of normal distribution, the command is: 
   ```python
   e = np.random.normal(0, 2, size=4)
   ```
   Note that this command generates a polynomial with coeffecients in a normal distribution of mean 0 and a standard deviation of 2
3. moreover, a binary vector can be generated as follows: 
   ```python
   s = np.random.randint(0,2,size=4)
   ```

## A R-LWE encryption scheme

Now we are able to generate R-LWE and LWE problems. 
The following encryption algorithm is based on R-LWE problem and has Homomorphic Encryption (HE) property.  

### Ex. 3 - Key Generation
Define the function keygen that generates the public key (a, b) and the secret key (s).
- **input**: seed, dim, modulus, poly_mod, where
    - seed: the seed for the random number generators. 
    - dim: size of the polynomials for the public and secret keys.
    - mod: coefficient modulus.
    - poly_mod: polynomial modulus.
- **Output**: (a,b), s 
   where:
    - a is a random polynomial of size dim modulus mod
    - e is a polynimial normally distributed of size dim
    - s is a binary polynomial of size dim  
    - b = -as-e
- Let the program print the values: a,e,s and b
- try Keygen with input: 
    - poly_mod = x^2 + 1
    - mod = 5
    - seed = 2
    - dim = 4
---
[Solution](Ex3.py) and [Example](Ex3.png)

---

## Encryption algorithm
In order to gain the HE property, we need to do as follows. 
- the messagge/plaintext pt is in Zt 
- the public key pk = (a,b)
- the ciphertext ct = (ct0,ct1) is a tuple of two polynomials where
    - `ct0 = a*u + e1 + delta*m mod q`
    - `ct1 = b*u + e2 mod q`

In particular, 
- u is a random binary polynomial
- delta = q // t 
- m is the constant polynomial m(x) = scaled_pt, where `scaled_pt = delta*m mod q`
  
  For example, if scaled_pt = 3, m(x) = 3 and if the polynomials have degree 2, then m = np.array([3,0,0])
- e1 and e2 are polynomials normally distributed


**Note**: the symbol `//` represents the integer division in python language.

### Ex. 4 - Encryption
Define the function encrypt. This algorithm follows the instructions above.
- **Input**: seed, pk, dim, q, t, poly_mod, pt where
  - seed: the seed for the random number generators.
  - pk: public key
  - dim: size of the polynomials.
  - t: message modulus.
  - q: coefficient modulus.
  - poly_mod: polynomial modulus.
  - pt: an integer in Zt representing the plaintext
- **Output**: ct (the ciphertext) 
- Then check that your implementation works using  keygen, encrypt that you created, and decrypt (below) with input parameters: 
  - poly_mod = x^4 + 1
  - mod = 6481
  - dim = 4
  - t = 179
  - the other parameters on your choice. 
---

**Here the descryption algorithm**
```python
def decrypt(sk, mod, t, poly_mod, ct):
	scaled_pt = polyadd_mod(polymul_mod(ct[1], sk, mod, poly_mod), ct[0], mod, poly_mod)
	delta = mod // t
	decrypted_poly = np.round(scaled_pt / delta) % t
	return int(decrypted_poly[0])
```

[Solution](Ex4.py) and [Example](Ex4.png)

### Ex. 5/HW. 1
The scheme above has some HE properties. 
Let a be an integer in Zt, ct = Enc(pt) a ciphertext and ct'= Enc(pt') another ciphertext, check that:
- `Dec(a + Enc(pt)) = Dec(Enc(pt+a))` 
- `Dec(Enc(pt) + Enc(pt')) = Dec(Enc(pt+pt'))`
- `Dec(a*Enc(pt)) = Dec(Enc(pt*a))`

Parameters: 
```python
# polynomial modulus degree
n = 2**4
# ciphertext modulus
q = 2**15
# plaintext modulus
t = 2**8
# polynomial modulus
poly_mod = np.array([1] + [0] * (n - 1) + [1])
```

Here the function that allows making the computations:

- Add a ciphertext ct and a plaintext pt:
```python
#Input:
#        ct: ciphertext.
#        pt: integer to add.
#        mod: ciphertext modulus.
#        t: plaintext modulus.
#        poly_mod: polynomial modulus.
#Output:
#        Tuple representing a ciphertext.

def add_plain(ct, pt, mod, t, poly_mod):

    dim = len(poly_mod) - 1
    # encode the integer into a plaintext polynomial
    m = np.array([pt] + [0] * (dim - 1), dtype=np.int64) % t
    delta = mod // t
    scaled_m = delta * m
    new_ct0 = polyadd_mod(ct[0], scaled_m, mod, poly_mod)
    return (new_ct0, ct[1])
```
- Add a ciphertext ct and a ciphertext ct2.
```python
#Input:
#        ct1, ct2: ciphertexts.
#        mod: ciphertext modulus.
#        poly_mod: polynomial modulus.
#Output:
#        Tuple representing a ciphertext.

def add_cipher(ct1, ct2, mod, poly_mod):

    new_ct0 = polyadd_mod(ct1[0], ct2[0], mod, poly_mod)
    new_ct1 = polyadd_mod(ct1[1], ct2[1], mod, poly_mod)
    return (new_ct0, new_ct1)
```
- Multiply a ciphertext and a plaintext.
```python
#Input:
#        ct: ciphertext.
#        pt: integer to multiply.
#        mod: ciphertext modulus.
#        t: plaintext modulus.
#        poly_mod: polynomial modulus.
#Output:
#        Tuple representing a ciphertext.

def mul_plain(ct, pt, mod, t, poly_mod):
    dim = len(poly_mod) - 1
    # encode the integer into a plaintext polynomial
    m = np.array([pt] + [0] * (dim - 1), dtype=np.int64) % t
    new_c0 = polymul_mod(ct[0], m, mod, poly_mod)
    new_c1 = polymul_mod(ct[1], m, mod, poly_mod)
    return (new_c0, new_c1)
```
---
**Note** We consider the case: Dec(a + Enc(pt)) = Dec(Enc(pt+a)). Note that `add_plain(ct, a, mod, t, poly_mod)` does not need pk, i.e., there is not encryption, while pk is needed in `encrypt(seed, pk, dim, mod, t, poly_mod, pt+a)`. 

---

[Solution](HW1.py) and [Example](HW1.png) for the first computation in the list. 



## References
* [numpy - polynomials](https://numpy.org/doc/stable/reference/routines.polynomials.html)
* [Regev and LWE in Python](https://gist.github.com/youben11/f00bc95c5dde5e11218f14f7110ad289)
* [Article](https://eprint.iacr.org/2012/144.pdf)
