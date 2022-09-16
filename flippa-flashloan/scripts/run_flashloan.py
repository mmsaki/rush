from brownie import accounts, config, network, interface, FlashloanAttacker

min_weth_balance = 5
tx_url = "https://goerli-optimism.etherscan.io/tx/{}"


def main():
    acct = accounts.add(config["wallets"]["from_key"])
    flashloan = FlashloanAttacker[len(FlashloanAttacker) -1]
    weth = interface.IWETH(config["networks"][network.show_active()]['WETH-TestnetMintableERC20'])
    # weth.balanceOf(flashloan) < min_weth_balance
    weth.approve(flashloan, min_weth_balance, {'from':acct})
    weth.transferFrom(acct, flashloan, min_weth_balance, {'from': acct})
    tx = flashloan.supplyAsset(weth, min_weth_balance, {'from': acct})
    print("You supplied an Asset! View your tx here: " + tx_url.format(tx.txid))
    return tx.info()
