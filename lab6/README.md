# Laboratory 6 - Fully Homomorphic Encryption and Applications

Fully Homomorphic Encryption (FHE) allows performing any kind of operation (unlimited sums and products). The ability to compute both sums and products on the same encrypted data.

* SUM = XOR
* PRODUCT = AND,

XOR, AND is Turing-complete and any function is a combination of XOR and AND gates.

![types_fhe.png](types_fhe.png)


## Main Applications using FHE

![app_fhe.png](app_fhe.png)

* **Outsourcing storage and computations** without revealing sensitive information:
cloud computing.
* **Private Information Retrieval (PIR)**: a server is holding a large database (e.g., the US patent database), and a client wants to retrieve one record of this database without the server learning which record was retrieved.
* **Multiparty computations**: mutually suspicious parties want to compute a common function on their joint input - next classes.

## Ex. 1 - Geolocation and Homomorphic Encryption (1p)
* check this [video](https://www.youtube.com/watch?v=ySl2ywGiFkw) (you can use 1.5x speed)
* check [repo](https://github.com/Georeactor/encrypted-geofence) and sources to know how they implement computations
* run basic demo

## Ex. 2 - play with sandbox env (1p)
* use this env [morfix.io](https://morfix.io/sandbox)
* create running FHE application

## Hw. 1 - FHE demo in python (2p)
* create and run demo FHE application in python
* you can use sources from previous labs
* you can use any lib you want
* demo should show step by step how it works or what it computes, or if the conditions are met

### Resources:
* [Awesome Homomorphic Encryption](https://github.com/jonaschn/awesome-he) - NOTE: It is trusted, it is from the inverstors of HE
* Google open-source [FHE](https://github.com/google/fully-homomorphic-encryption)
