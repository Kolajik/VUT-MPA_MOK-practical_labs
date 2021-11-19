from src.classes.Transaction import Transaction as T

if __name__ == '__main__':
    t = T(8920)

    amountOfTrx = getattr(t, 'amount')
    uuidOfTrx = getattr(t, 'trxId')

    print(amountOfTrx)
    print(uuidOfTrx)
