import Transaction
import hashlib
import time
import json


class Blockchain:

    def __init__(self):
        self.counter = -1
        self.difficulty = 0
        self.chain = []
        self.mempool = []

    def new_block(self, previous_hash=None, difficulty=0):
        self.counter += 1

        str_trx = []
        for trx in self.mempool:
            str_trx.append(str(trx))

        block = {
            "index": self.counter,
            "timestamp": time.strftime("%m/%d/%Y, %H:%M:%S"),
            "difficulty": self.difficulty,
            "transactions": self.mempool,
            "transactions_hash": hashlib.sha3_256(str(self.mempool).encode('utf-8')),
            "previous_hash": previous_hash or hashlib.sha3_256(str(str_trx).encode()),
            "nonce": 0
        }
        self.mempool = []

        self.chain.append(block)

        # json.dump(block).encode()

    def search_transaction(self, transaction_id):
        if len(self.chain) == 0:
            pass
        else:
            i = 0
            for block in self.chain:
                j = 0
                for transaction in block['transactions']:
                    if transaction.transaction_id == transaction_id:
                        print("Transaction you're looking for: {}\nIn chain with index {}".format(
                            self.chain[i]['transactions'], self.chain[i]['index']))
                        break
                    else:
                        j += 1
                i += 1

    def put_trx_in_block(self, transaction):
        if isinstance(transaction, Transaction.Transaction):
            self.mempool.append(transaction)
        else:
            print("Transaction {} not of a type Transaction.\nActual type: {}".format(transaction, type(transaction)))

    def print_blocks(self):
        print(self.chain)

    def set_difficulty(self, diff):
        self.difficulty = diff
