# The script is pretty straightforward. 
# We first deploy the SimpleSwap contract and then call the swapWETHForDAI function. 
# The function takes in the amount of WETH to swap for DAI. 
# The function will then swap the WETH for DAI and return the transaction.


from brownie import interface
from scripts.aave.helper_functions import get_account, get_weth, get_token
from brownie import SimpleSwap
from brownie.network import priority_fee
from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie.network.gas.strategies import GasNowStrategy
from brownie.network import gas_price

priority_fee("2 gwei")
gas_strategy = GasNowStrategy("fast")
gas_price(gas_strategy)

dev = get_account()
router = interface.IV3SwapRouter("0xE592427A0AEce92De3Edee1F18E0157C05861564")
weth = interface.IWETH9("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
dai = interface.IERC20("0x6B175474E89094C44Da98b954EedeAC495271d0F")
amount = 0.1 * 10**18


def main():
    # check balance
    print("WETH balance: ", weth.balanceOf(dev))
    print("DAI balance: ", dai.balanceOf(dev))

    # deploy simple swap
    contract = SimpleSwap.deploy(router, {"from": dev})

    # get weth
    weth.deposit({"from": dev, "value": amount})

    # approve router to spend weth
    weth.approve(contract, amount * 2, {"from": dev})

    # swap weth for dai
    tx = contract.swapWETHForDAI(amount, {"from": dev})

    # check balance
    print("WETH balance: ", weth.balanceOf(dev))
    print("DAI balance: ", dai.balanceOf(dev))

    return tx


if __name__ == "__main__":
    main()


