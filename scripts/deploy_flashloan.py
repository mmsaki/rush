from brownie import RushFlashLoan, RushSimpleFlashLoan
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
    dev = get_account()
    print(f"""===============================================""")
    print(f"""Deploying Simple Rush flashloan receiver contract ...""")
    print(f"""===============================================""")
    flashloan = RushSimpleFlashLoan.deploy(address_provider, {"from": dev})
    print(f"View contract on Optimism Goerli 📍 📍 📍 📍 {tx_url.format(flashloan.address)}")
    return flashloan.tx.info()

def batch_flashloan():
    dev = get_account()
    print(f"""===============================================""")
    print(f"""Deploying Rush flashloan receiver contract ...""")
    print(f"""===============================================""")
    flashloan = RushFlashLoan.deploy(address_provider, {"from": dev})
    print(f"View contract on Optimism Goerli 📍 📍 📍 📍 {tx_url.format(flashloan.address)}")
    return flashloan.tx.info()

def main():
    batch_flashloan()
    simple_flashloan()
    ascii_art()


