from brownie import accounts, config, network, interface, RushSimpleFlashLoan
from scripts.helper_functions import get_address_provider, get_token, get_account
import web3

tx_url = "https://goerli-optimism.etherscan.io/tx/{}"

pool = interface.IPool(get_address_provider().getPool())

flashloan_receiver = RushSimpleFlashLoan[len(RushSimpleFlashLoan) -1]

usdc = get_token("USDC")

usdc_amount = 10000000 * 10** usdc.decimals()


def run_flashloan():
    acct = get_account()
    receiver = flashloan_receiver
    assets = usdc
    amount = usdc_amount
    params = receiver.address
    referral = 0
    tx = pool.flashLoanSimple(receiver, assets, amount, params, referral, {"from": acct})
    
    tx.wait(3)
    print(f"Congrats! You have flipped a flashloan. Check it out! {tx_url.format(tx.txid)}")
    return tx

def main():
    run_flashloan()