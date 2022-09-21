from brownie import accounts, config, network, interface

tx_url = "https://goerli-optimism.etherscan.io/tx/{}"

def main():
    get_weth()

def get_weth():
    amount = 4 * 10 ** 18
    acct = accounts.add(config["wallets"]["from_key"]) 
    weth = interface.IWETH(config["networks"][network.show_active()]['WETH-TestnetMintableERC20'])
    tx = weth.deposit({"from": acct, "value": amount})
    print(f"Received {amount} WETH")
    print("View your tx here: " + tx_url.format(tx.txid))
    return tx.info()

def withdraw_eth():
    amount = 10 
    acct = accounts.add(config["wallets"]["from_key"]) 
    weth = interface.IWETH(config["networks"][network.show_active()]['WETH-TestnetMintableERC20'])
    tx = weth.withdraw(amount, {"from": acct })
    print(f"Received {amount} ETH")
    print("View your tx here: " + tx_url.format(tx.txid))
    return tx.info()
