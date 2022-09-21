from scripts.helper_functions import *
from brownie import interface

token_name = "USDT"
amount = 45000000000

def mint_token(token_name, amount):
    acct = get_account()
    token = get_token(token_name)
    mintable_token = interface.IMintableERC20(token.address)
    tx = mintable_token.mint(amount * 10 ** token.decimals(), {'from': acct})
    return tx

def main():
    mint_token(token_name, amount)