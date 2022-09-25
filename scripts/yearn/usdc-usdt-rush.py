from brownie import interface, Registry, rToken
from scripts.yearn.helper_functions import *


dev = get_account()
gov = get_account()

usdt = get_token("USDT")
usdt.balanceOf(dev)

registry = Registry.at("0xe3A8d750a7B2092B3cb7Ba541236BB929427Bd5F")


def main():
    deploy_r_token_wrapper(usdt, registry, gov)
    usdt_rush = rToken[-1]

    deploy_vault(dev)

    usdt_vault = Vault[-1]
    intialize_r_vault(usdt_vault, usdt_rush, gov, gov, "USDT-Rush yVault", "yvUSDT-Rush", gov, gov)