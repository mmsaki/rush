from brownie import RushToken, Vault, accounts, network
from helper_functions import *
import click

y_vault = Vault[-1]
dev = accounts.load(click.prompt("Account", type=click.Choice(accounts.load())))
url = "https://goerli-optimism.etherscan.io/tx/{}"

def intialize_y_vault():
    print(f"Dev is initializing Rush yVault ..")
    tx = Vault[-1](RushToken[-1], dev, dev, "⤷Rush yVault", "▨yvRush", dev, dev, {'from': dev})
    print("View your tx here: " + url.format(tx.txid))
    return tx



def set_gov():
    print(f"{y_vault.setGovernance.info()}")

    print(f"Setting vault governance...")
    tx = y_vault.setGovernance(dev, {"from": dev})
    tx.wait(1)
    print("View your tx here: " + url.format(tx.txid)

    return tx

def accept_gov():
    print(f"{ y_vault.acceptGovernance.info()}")

    print(f"Accepting vault governance...")
    tx = y_vault.acceptGovernance({'from': dev})
    tx.wait(1)
    print("View your tx here: " + url.format(tx.txid)

    return tx 

def set_deposit_limit():
    print(f"{Vault[-1].setDepositLimit.info()}")

    print(f"Setting vault deposit Limit to half total supply...")
    return Vault[-1].setDepositLimit(30000*10**18, {'from': dev})

def main():
    intialize_y_vault()
    set_gov()
    accept_gov()
    set_deposit_limit()


# vault = Vault[-1]
# vault.initialize(usdc, dev, dev, "Rush yVault", "yvRush", dev, dev, {"from": dev}) 
# vault.setGovernance(dev, {"from": dev})
# vault.setManagement(dev, {"from": dev})
# vault.setRewards(dev, {"from": dev})
# vault.setManagementFee(1, {"from": dev})
# vault.setGuardian(dev, {"from" : dev})
# vault.performanceFee()
# vault.pricePerShare()
# vault.activation()