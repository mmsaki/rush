from brownie import Vault, accounts, Registry
from scripts.yearn.helper_functions import new_experimental_vault, get_token, new_release
import click

dev = accounts.load("0","0")
gov = accounts.load("0","0")
reg = Registry.at("0xe3A8d750a7B2092B3cb7Ba541236BB929427Bd5F")
guardian = dev
rewards = gov
token = get_token("USDC")
vault = Vault.at("0x22f72c8F00A8581594AF8A8A33Db8DDBAa7b14a6")

def experimental_vault():
    print(f"Dev is initializing Rush yVault ..")
    tx = new_experimental_vault(token, reg, vault, gov, guardian, rewards, vault.name(), vault.symbol(), 0)
    return tx

def new_vault_release():
    tx = new_release(reg, vault, gov)
    return tx
    
def register_vault():
    tx = reg.newVault(vault, dev, dev, vault.name(), vault.symbol(), 0, {'from': dev})
    return tx 

def endorse_vault(reg, vault, gov):
    return reg.endorseVault(vault, 0,{'from': gov})

def main ():
    experimental_vault()
    register_vault()
    endorse_vault()