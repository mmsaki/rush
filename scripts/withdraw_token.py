from scripts.deploy_flashloanhelper_functions import get_token, get_lending_pool, get_account

# Enter string of token i.e "DAI", "USDC" "USDT" , see config.yaml for more
def withdraw_token(_token, amount):
    dev = get_account()
    lending_pool = get_lending_pool()
    token = get_token(_token)
    tx = lending_pool.withdraw(token.address, amount, account, {"from": dev})
    return  web3.eth.get_transaction_receipt(tx)