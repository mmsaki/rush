from brownie import accounts, config, network, interface

amount = 100
tx_url = "https://goerli-optimism.etherscan.io/tx/{}"

def main():
    get_weth()

def get_weth():
    acct = accounts.add(config["wallets"]["from_key"]) 
    weth = interface.IWETH(config["networks"][network.show_active()]['WETH-TestnetMintableERC20'])
    tx = weth.deposit({"from": acct, "value": amount})
    print(f"Received {amount} WETH")
    print("View your tx here: " + tx_url.format(tx.txid))
    return tx.info()
