# Ethereum_U2F_Trigger  
## Environment  
### web3
```sh
pip install web3
```
or follows:  
https://web3py.readthedocs.io/en/stable/web3.eth.html#web3.eth.Eth.get_block_transaction_count  

### geth   
start geth following:  
https://geth.ethereum.org/docs/getting-started

###  Infura
Create an accound on Infura  
https://infura.io/dashboard/ethereum/40cbe38b88ce4754b5883109b6fbd3ae/settings

### SQLite
Build SQLite following:  
https://www.sqlite.org/  


## Structure
Reference:  
https://github.com/validitylabs/EthereumDB  by Aleksandra Sokolowska

U2F_Trigger.py:  
	-functionality: The simple version U2F trigger, which triggers if there are too many out trasactions in the past defined days  
	-author: Mu Changrui  

updateDataBase.py
	-functionality: Access blocks within recent days, and stored in database  
	-author: Mu Changrui


organize.py:  
	-functionality: store functions for editting SQLite  
	-author: Aleksandra Sokolowska  
  
sql_helper.py:  
	-functionality: daos  
	-author: Aleksandra Sokolowska  





