""" 
Author: Mu Changrui
"""
from organize import *
def updateDataBase(forwardDays):
	from web3 import Web3
	import time
	import sqlite3 as sq3
	#uncomment one of the options below
	# 1. connection via Infura
	web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/40cbe38b88ce4754b5883109b6fbd3ae"))
	# 2. or connection via local node 
	#web3 = Web3(Web3.IPCProvider('/your-path-to/geth.ipc'))
	newestBlockNumber = web3.eth.blockNumber
	# forwardDays is forwardDays* (24h/day) * (60 min/h) *(60 s/min)
	# Ethereum Update Averagely 1 per 10 seconds, here we catch an upperbound, hence multiply an additional 3
	nBlocks = forwardDays*24*60*60*3/10

	startBlockNumber = newestBlockNumber - nBlocks

	conn = sq3.connect("blockchain.db")
	cur = conn.cursor()

	# delete old block to save storage in sql
	#cur.execute("DELETE FROM Quick WHERE blockNumber < "+str(startBlockNumber))
	#cur.execute("DELETE FROM TX WHERE blockNumber < "+str(startBlockNumber))
	#cur.execute("DELETE FROM Block WHERE blockNumber < "+str(startBlockNumber))
	#conn.commit()

	# avoid repeat graping block
	cur.execute("SELECT MAX(blockNumber) FROM Quick")
	a = cur.fetchall()
	print(a)
	startBlockNumber = max(startBlockNumber,a[0][0]+1)
	conn.close()
	if startBlockNumber > newestBlockNumber:
		return 0

	#define tables that will go to the SQLite database
	table_quick = []
	table_tx = []
	table_block = []
	count = 0
	output_every = 2
	start_time = time.time()
	for block in range(startBlockNumber, newestBlockNumber+1):
		print(block)
		block_table, block_data = order_table_block(block,web3)
		#list of block data that will go to the DB
		table_block.append(block_table)

		#all transactions on the block
		for hashh in block_data['transactions']:
			#print(web3.toHex(hashh))
			quick_table, tx_data = order_table_quick(hashh,block, web3)
			table_quick.append(quick_table)

			#list of tx data that will go to the DB
			TX_table = order_table_tx(tx_data,hashh, web3)
			table_tx.append(TX_table)
		count = count + 1
		#print(count)
		#dump output every 2 blocks
		if (count % output_every) == 0:
			execute_sql(table_quick, table_tx, table_block)
			#free up memory
			del table_quick
			del table_tx
			del table_block
			table_quick = []
			table_tx = []
			table_block = []
			#update the current block number to a file
			with open('lastblock.txt', 'w') as f:
				f.write("%d" % block)
		if (count % 10) == 0:
			end = time.time()
			with open('timeperXblocks.txt', 'a') as f:
				f.write("%d %f \n" % (block, end-start_time))
		if (count % 100) == 0:
			print("100 new blocks completed.")



