import threading
from tracemalloc import stop
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://speedy-nodes-nyc.moralis.io/..."))
private_key = "<Your_Private_Key"
pub_key ="<Your_wallet>"

recipient_pub_key = "<Recipient_wallet>"
def loop():
    while True:
        balance = w3.eth.get_balance(pub_key)
        print()
        print(balance)
        gasPrice = w3.toWei('1100', 'gwei')
        gasLimit = 21000
        nonce = w3.eth.getTransactionCount(pub_key)
        tx = {
            'chainId': 3,
            'nonce': nonce,
            'to': recipient_pub_key,
            'value': balance-gasLimit*gasPrice,
            'gas': gasLimit,
            'gasPrice': gasPrice
        }

        try:
         if balance > 0:
            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(w3.toHex(tx_hash))
        except:
            print("insufficient funds")

threading.Thread(target=loop, daemon=True).start()
input('Press Enter to exit.')
