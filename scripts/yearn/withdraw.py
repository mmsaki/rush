from brownie import Vault, accounts
from scripts.yearn.helper_functions import *

url = "https://goerli-optimism.etherscan.io/tx/{}"
dev = get_account()
vault = Vault.at("0x75CDC61d8d51A669Ea0E1b525f9D3905cC049866")
token = get_token("USDT")

amount = 1000000000 * 10**vault.decimals()

def withdraw():
    print(f"withdrawing tokens to yVault...")
    tx = withdraw_from_vault(vault, amount, dev)
    print("View your tx here: " + url.format(tx.txid))
    return tx


def main():
    withdraw()