from brownie import Vault, accounts, registry
import click

dev = accounts.load("0","0")

def experimental_vault():
    print(f"Dev is initializing Rush yVault ..")
    tx = registry.newExperimentalVault(Vault[-1].address, dev, dev, dev, Vault[-1].name(), Vault[-1].symbol(), 0, {'from': dev})
    return tx

def register_vault():
    tx = registry.newVault(Vault[-1], dev, dev, Vault[-1].name(), Vault[-1].symbol(), 0, {'from': dev})
    return tx 

def main ():
    experimental_vault()
    register_vault()