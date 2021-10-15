

import math
import random
import numpy as np
from random import randint
import base64
import binascii
from scipy import linalg
#from libLLL import *


"""
	Here we generate a public and private key using an orthogonal private key 
	and a nearly parallel public key 
	n is the security parameter given 
"""
def keyGeneration(n):
    privateB=[]
    ratio = 1
    """
    while True:
        #iterations = iterations + 1
        privateB=np.random.random_integers(-10,10,size=(n,n))
        #privateB=gram_schmidt_columns(privateB)
        privateB=np.array( lll_reduction(privateB))
        ratio =hamdamard_ratio(privateB,n)
        print(ratio)
        if(ratio >= .8 and ratio <= 1):
        	privateB=privateB.astype(int)
        	break
	"""
    privateB=np.identity(n)
    #privateB =linalg.orth(np.random.random_integers(-10,10,size=(n,n))).astype(int)

    while True:
        badVector = rand_unimod(n)
        temp=np.matmul(privateB,badVector)
        ratio = hamdamard_ratio(temp,n)
        if ratio <= .1:
            publicB=temp
            break
    return privateB,publicB,badVector

def gram_schmidt_columns(X):
    Q, R = np.linalg.qr(X)
    return Q

"""
	This function is used to determine how orthogonal the matrix is 
	close to 1 = orthogonal
	close to 0 = parallel vectors
"""
def hamdamard_ratio(basis,dimension):
	detOfLattice = np.linalg.det(basis)
	mult=1
	for v in basis:
		mult = mult * np.linalg.norm(v)#(np.sqrt((v.dot(v))))
	hratio = (detOfLattice / mult) ** (1.0/dimension)
	return hratio

"""
	This method is used to encrypt a text file with the public vector
	Multiplication should be performed as
		v_1 * b_1  + v_2 * b_2 ... V_n * B_n

"""
def encrypt(fileName, publicB):#needs extension to new keys <---
	#publicB = [[1,45],[1,-45]] # making my own public basis b
	encoded = []
	with open(fileName,'r') as f:
		for line in f:
			for c in line:
				encoded.append(base64.b64encode(bytes( c,"utf-8") ) )
	binaryMessage=[]
	for i in range(len(encoded)):
		binaryMessage.append( binascii.a2b_base64(encoded[i]) )

	encrypted_ints = []
	for i in range(len(encoded)):
		encrypted_ints.append( int.from_bytes(binaryMessage[i],byteorder='little') )

	ciphertext =[]
	for i in range(len(encoded)):
		# ciphertext.append(np.multiply( int.from_bytes(encrypted[i],byteorder='little') ,publicB[i]))
		ciphertext = np.matmul( encrypted_ints, publicB)
	random_vector = np.random.randint(-10,10,size=(1,len(publicB)))
	# ciphertext = ciphertext + random_vector


	return ciphertext

"""
	This will take a cyphertext and revert it back to its original form
"""
def decrypt(cipherText,privateBasis,publicB,unimodular):

    A = privateBasis
    x = cipherText
    BPRIME = np.linalg.inv(A)
    BB = np.matmul(BPRIME,x)
    unimodular1 = np.linalg.inv(unimodular)
    m =np.round(np.matmul(BB,unimodular1)).astype(int)#np.round(np.matmul(BB,unimodular1)).astype(int)

    return m


"""
	This function will create a random unimodular matrix that will be used to transform our public vector
"""
def rand_unimod(n):
    random_matrix = [ [np.random.randint(-10,10,) for _ in range(n) ] for _ in range(n) ]
    upperTri = np.triu(random_matrix,0)
    lowerTri = [[np.random.randint(-10,10) if x<y else 0 for x in range(n)] for y in range(n)]

    #we want to create an upper and lower triangular matrix with +/- 1 in the diag
    for r in range(len(upperTri)):
    	for c in range(len(upperTri)):
    		if(r==c):
    			if bool(random.getrandbits(1)):
    				upperTri[r][c]=1
    				lowerTri[r][c]=1
    			else:
    				upperTri[r][c]=-1
    				lowerTri[r][c]=-1
    uniModular = np.matmul(upperTri,lowerTri);
    return uniModular



