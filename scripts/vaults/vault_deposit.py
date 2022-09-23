from brownie import Vault, accounts, registry

dev = accounts.load("0","0")
amount = 100 * 10**18

def deposit():
    print(f"Depositing tokens to yVault...")
    tx = Vault.deposit(amount, dev, {'from': dev})
    return tx


def main():
    deposit()