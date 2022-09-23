from brownie import interface, Registry, rToken
from helper_functions import *


dev = get_dev_account()
gov = get_gov_account()

usdt = get_token("USDT")
usdt.balanceOf(dev)

registry = Registry[-1]


def main():
    usdt_wrapper_tx = deploy_r_token_wrapper(usdt, registry, gov)
    usdt_wrapper_tx.wait(1)
    usdt_rush = rToken[-1]

    usdt_vault_tx = deploy_vault(dev)
    usdt_vault_tx.wait()

    usdt_vault = Vault[-1]
    intialize_r_vault(usdt_vault, usdt_rush, gov, gov, "USDC-Rush yVault", "yvUSDC-Rush", gov, gov)