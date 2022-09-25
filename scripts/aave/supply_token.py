from brownie import config, accounts, interface, network
from scripts.aave.helper_functions import get_address_provider, get_token, get_account, get_lending_pool

amount = 1001490533000000000000000
token_name = "SUSD"

# Accepts token_name as string
def supply_token():
    dev = get_account()
    token = get_token(token_name)
    provider = get_address_provider()
    pool = get_lending_pool()
    approval_tx = token.approve(pool, amount, {"from": dev})
    tx = pool.supply(token, amount, dev, 0, {"from": dev})
    return tx

# Accepts token name as string
def main():
    supply_token()