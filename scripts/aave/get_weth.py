from brownie import accounts, config, network, interface

url = "https://goerli-optimism.etherscan.io/tx/{}"

def main():
    get_weth()

def get_weth():
    amount = 4 * 10 ** 18
    dev = accounts.add(config["wallets"]["from_key"]) 
    weth = interface.IWETH(config["networks"][network.show_active()]['WETH-TestnetMintableERC20'])
    tx = weth.deposit({"from": dev, "value": amount})
    print(f"Received {amount} WETH")
    print("View your tx here: " + url.format(tx.txid))
    return tx.info()

def withdraw_eth():
    amount = 10 
    dev = accounts.add(config["wallets"]["from_key"]) 
    weth = interface.IWETH(config["networks"][network.show_active()]['WETH-TestnetMintableERC20'])
    tx = weth.withdraw(amount, {"from": dev })
    print(f"Received {amount} ETH")
    print("View your tx here: " + url.format(tx.txid))
    return tx.info()
