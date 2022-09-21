from scripts.deploy_flashloanhelper_functions import get_token, get_lending_pool, get_account

# Enter string of token i.e "DAI", "USDC" "USDT" , see config.yaml for more
def repay_token(_token, amount):
    account = get_account()
    token = get_token(_token)
    lending_pool = get_lending_pool()

    print(f"Approving ERC20 token to spender address {lending_pool} ...")
    approval_tx = token.approve(lending_pool, amount, {"from": account})
    approval_tx.wait(1)
    
    print(f"Now repaying loan using of {token} with amount {amount} Wei.")
    tx = lending_pool.repay(token.address, amount, 2, acct, {'from': acct})
    return tx.info()