import uuid


class Transaction:

    def __init__(self, amount):
        self.amount = amount
        self.trxId = uuid.uuid1()
