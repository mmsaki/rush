from brownie import interface
from scripts.aave.helper_functions import get_account
from brownie import MultiSwaps
from brownie.network import priority_fee
from brownie.network.gas.strategies import GasNowStrategy
from brownie.network import gas_price

priority_fee("2 gwei")
gas_strategy = GasNowStrategy("fast")
gas_price(gas_strategy)

dev = get_account()
router = interface.IV3SwapRouter("0xE592427A0AEce92De3Edee1F18E0157C05861564")
weth = interface.IWETH9("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
dai = interface.IERC20("0x6B175474E89094C44Da98b954EedeAC495271d0F")
usdc = interface.IERC20("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
amount_dai = 6000 * 10**18

def main():
    # check balance
    print("WETH balance: ", weth.balanceOf(dev))
    print("DAI balance: ", dai.balanceOf(dev))

    # deploy simple swap
    contract = MultiSwaps.deploy(router, {"from": dev})

    # approve router to spend dai with 1.1x slippage
    dai.approve(contract, amount_dai * 1.1, {"from": dev})

    # swap weth for dai
    tx = contract.swapExactInputMultihop(amount_dai, {"from": dev})

    # check balance
    print("WETH balance: ", weth.balanceOf(dev))
    print("DAI balance: ", dai.balanceOf(dev))

    return tx

