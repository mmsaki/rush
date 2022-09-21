from brownie import FlashLoanReceiver, FlashLoanSimpleReceiver
from scripts.helper_functions import get_account, get_address_provider

def ascii_art():

    print("""       
     ___           ___   ____    ____  _______ 
    /   \         /   \  \   \  /   / |   ____|
   /  ^  \       /  ^  \  \   \/   /  |  |__   
  /  /_\  \     /  /_\  \  \      /   |   __|  
 /  _____  \   /  _____  \  \    /    |  |____ 
/__/     \__\ /__/     \__\  \__/     |_______|
                                               
                
                      )     
    )           )  ( /( (   
   (     (   ( /(  )\()))\  
   )\  ' )\  )(_))((_)\((_) 
 _((_)) ((_)((_)_ | |(_)(_) 
| '  \()(_-</ _` || / / | | 
|_|_|_| /__/\__,_||_\_\ |_| 
                            

    """)

address_provider = get_address_provider()
tx_url = "https://goerli-optimism.etherscan.io/address/{}"

def simple_flashloan():
    acct = get_account()
    print(f"""===============================================""")
    print(f"""Deploying Simple flashloan receiver contract ...""")
    print(f"""===============================================""")
    flashloan = FlashLoanSimpleReceiver.deploy(address_provider, {"from": acct})
    print(f"View contract on Optimism Goerli 📍 📍 📍 📍 {tx_url.format(flashloan.address)}")
    return flashloan.tx.info()

def batch_flashloan():
    acct = get_account()
    print(f"""===============================================""")
    print(f"""Deploying Batch flashloan receiver contract ...""")
    print(f"""===============================================""")
    flashloan = FlashLoanReceiver.deploy(address_provider, {"from": acct})
    print(f"View contract on Optimism Goerli 📍 📍 📍 📍 {tx_url.format(flashloan.address)}")
    return flashloan.tx.info()

def main():
    batch_flashloan()
    simple_flashloan()
    ascii_art()


