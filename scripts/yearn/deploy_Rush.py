from brownie import Registry, accounts, network, RushToken
from scripts.yearn.helper_functions import get_account, deploy_rush_token

import click

def deploy_token():
    dev = get_account()

    print(f"Dev is deploying Registry ..")
    tx = deploy_rush_token("Rush®", "®🎠", 6000, dev)
    return tx

def main():
    deploy_rush_token()

def get_registry():
    return Registry[-1]

