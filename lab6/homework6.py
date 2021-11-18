import phe


def bankOperation(pub_key, secretAmount):
    feeForExchange = 300
    exchangeRate = 1.9

    encFee = pub_key.encrypt(feeForExchange)

    resultOperation = secretAmount - encFee
    resultOperation *= exchangeRate

    return resultOperation


if __name__ == '__main__':
    pub_key, priv_key = phe.generate_paillier_keypair()

    print("Public key of paillier: {}\nPrivate key of paillier: {}\n".format(pub_key, priv_key))

    transactionAmount = 15899
    secretTransactionAmount = pub_key.encrypt(transactionAmount)
    print("Transaction amount: {}\nSecret transaction amount: {}\n".format(transactionAmount,
                                                                           str(secretTransactionAmount.ciphertext())[
                                                                           :32]))

    amountRetrievedFromBank = bankOperation(pub_key, secretTransactionAmount)
    decryptedAmount = priv_key.decrypt(amountRetrievedFromBank)
    print("Information retreived from bank: {}\nAmount decrypted: {}".format(str(amountRetrievedFromBank.ciphertext())[:32],decryptedAmount))