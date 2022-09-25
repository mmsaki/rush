from scripts.aave.helper_functions import get_token, get_lending_pool, get_account


# Enter string of token i.e "DAI", "USDC" "USDT" , see config.yaml for more
token_name = "AAVE"
amount = 4198416377744149752773

def withdraw_token():
    dev = get_account()
    lending_pool = get_lending_pool()
    token = get_token(token_name)
    tx = lending_pool.withdraw(token.address, amount, dev, {"from": dev})
    return  tx

def main():
    withdraw_token()