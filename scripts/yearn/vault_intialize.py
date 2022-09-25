from brownie import RushToken, Vault, accounts, network
from scripts.yearn.helper_functions import *
import click

vault = Vault.at("0x34285280703156Cb15185a76af96EE7b4fC3307A")
token = get_token("AAVE")
vault_name = "Rush AAVe"
vault_symbol = "vrAAVE"
gov = get_account()
dev =get_account()
rewards = gov
guardian = dev
managment = gov

url = "https://goerli-optimism.etherscan.io/tx/{}"

def intialize_vault():
    print(f"Dev is initializing Rush yVault ..")
    tx = vault.initialize(token, gov, rewards, vault_name, vault_symbol, guardian, managment, {'from': dev})
    print("View your tx here: " + url.format(tx.txid))
    return tx



def set_gov():
    print(f"{vault.setGovernance.info()}")
    print(f"Setting vault governance...")
    tx = vault.setGovernance(gov, {"from": gov})
    tx.wait(1)
    print(f"View your tx here: + {url.format(tx.txid)}")
    return tx

def accept_gov():
    print(f"{ vault.acceptGovernance.info()}")

    print(f"Accepting vault governance...")
    tx = vault.acceptGovernance({'from': gov})
    tx.wait(1)
    print(f"View your tx here: + {url.format(tx.txid)}")

    return tx 

def set_deposit_limit():
    print(f"{vault.setDepositLimit.info()}")

    print(f"Setting vault deposit Limit to half total supply...")
    return vault.setDepositLimit(18100323156889900*10**18, {'from': dev})

def main():
    intialize_vault()
    set_gov()
    accept_gov()
    set_deposit_limit()


# vault = vault
# vault.initialize(usdc, dev, dev, "Rush yVault", "yvRush", dev, dev, {"from": dev}) 
# vault.setGovernance(dev, {"from": dev})
# vault.setManagement(dev, {"from": dev})
# vault.setRewards(dev, {"from": dev})
# vault.setManagementFee(1, {"from": dev})
# vault.setGuardian(dev, {"from" : dev})
# vault.performanceFee()
# vault.pricePerShare()
# vault.activation()