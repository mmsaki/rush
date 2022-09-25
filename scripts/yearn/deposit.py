from brownie import Vault, accounts
from scripts.yearn.helper_functions import *

url = "https://goerli-optimism.etherscan.io/tx/{}"
dev = get_account()

reg = Registry.at("0xe3A8d750a7B2092B3cb7Ba541236BB929427Bd5F")
token = get_token("USDT")
vault = Vault.at(reg.latestVault(usdt))

amount = 100000 * 10**vault.decimals()

def deposit():
    print(f"Depositing tokens to yVault...")
    approve_token_to_vault(token, vault, amount, dev)
    recipient = dev
    tx = deposit_to_vault(vault, amount, recipient)
    print("View your tx here: " + url.format(tx.txid))
    return tx


def main():
    deposit()


    