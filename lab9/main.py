import Transaction as T, Blockchain as B

if __name__ == '__main__':
    genesis_trx = T.Transaction("MINER", "Satoshi", "1500 MOK")
    blockchain = B.Blockchain()
    blockchain.put_trx_in_block(genesis_trx)
    blockchain.new_block(previous_hash="GEN_BLOCK")

    t1 = T.Transaction("Satoshi", "Mike", '5 MOK')
    t2 = T.Transaction("Mike", "Satoshi", '1 MOK')

    blockchain.put_trx_in_block(t1)
    blockchain.put_trx_in_block(t2)
    blockchain.new_block()

    print("Blockchain: \n{}\n".format(blockchain.print_blocks()))
    blockchain.search_transaction('ecba2d')
