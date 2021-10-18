#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Peter Cibik"
__email__ = "xcibik00@vutbr.cz"

# Caesar
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CAESAR_KEY = 3

# Caesar - 1
CAESAR_INPUT_MESSAGE_1 = "THISISMESSAGE"
CAESAR_CIPHER_TEXT_1 = "WKLVLVPHVVDJH"

# Caesar - 2
CAESAR_INPUT_MESSAGE_2 = "CAESARISTHEBEST"
CAESAR_CIPHER_TEXT_2 =  "FDHVDULVWKHEHVW"

# Caesar - 3
CAESAR_ADD_HOMOMORPTIC_TEST_M_1_1 = "HELLO"
CAESAR_ADD_HOMOMORPTIC_TEST_M_1_2 = "WORLD"
CAESAR_ADD_HOMOMORPTIC_EXPECTED_OUTPUT_1 = "DSCWR"

# Caesar - 4
CAESAR_ADD_HOMOMORPTIC_TEST_M_2_1 = "MPA"
CAESAR_ADD_HOMOMORPTIC_TEST_M_2_2 = "MOK"
CAESAR_ADD_HOMOMORPTIC_EXPECTED_OUTPUT_2 = "YDK"

# RSA
RSA_r = 11
RSA_s = 13
RSA_n = RSA_r * RSA_s
# private key
RSA_sk = 7
# public key
RSA_pk = 103

# RSA - 1
RSA_m1_1 = 28
RSA_m2_1 = 33
RSA_MUL_HOMOMORPHIC_EXPECTED_OUTPUT_1 = 66

# RSA - 2
RSA_m1_2 = 56
RSA_m2_2 = 256
RSA_MUL_HOMOMORPHIC_EXPECTED_OUTPUT_2 = 36
