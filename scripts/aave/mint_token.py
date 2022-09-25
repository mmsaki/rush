from scripts.aave.helper_functions import *
from brownie import interface

token_name = "WETH"
amount = 45000

def mint_token(token_name, amount):
    dev = get_account()
    token = get_token(token_name)
    mintable_token = interface.IMintableERC20(token.address)
    tx = mintable_token.mint(amount * 10 ** token.decimals(), {'from': dev})
    return tx

def main():
    mint_token(token_name, amount)