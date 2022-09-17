from brownie import accounts, config, network, interface, FlashloanAttacker

address_provider = interface.IPoolAddressesProvider(config["networks"][network.show_active()]["PoolAddressesProvider-Optimistic"])
tx_url = "https://goerli-optimism.etherscan.io/address/{}"

def main():
    acct = accounts.add(config["wallets"]["from_key"])  
    flashloan = FlashloanAttacker.deploy(address_provider, {'from': acct})
    print(f"Deployed FlashloanAttacker Contract")
    print("View your contract here: " + tx_url.format(flashloan.address))
    return flashloan.tx.info()
