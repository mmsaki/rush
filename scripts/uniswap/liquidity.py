from brownie import interface
from scripts.aave.helper_functions import get_account, get_weth, get_token
from brownie import LiquidityExamples
from brownie.network import priority_fee
from brownie.network.gas.strategies import GasNowScalingStrategy
from brownie.network.gas.strategies import GasNowStrategy
from brownie.network import gas_price

priority_fee("2 gwei")
gas_strategy = GasNowStrategy("fast")
gas_price(gas_strategy)

dev = get_account()
router = interface.IV3SwapRouter("0xE592427A0AEce92De3Edee1F18E0157C05861564")
dai = interface.IERC20("0x6B175474E89094C44Da98b954EedeAC495271d0F")
usdc = interface.IERC20("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
contract = LiquidityExamples.deploy("0xC36442b4a4522E871399CD717aBDD847Ab11FE88", {'from': dev})
dai.transfer(contract, 1000 * 10**18, {'from': dev})
usdc.transfer(contract, 1000 * 10**6, {'from': dev})
contract.mintNewPosition( 1000 * 10**18, 1000 * 10**6, {'from': dev})
dai.balanceOf(dev)
usdc.balanceOf(dev)

# if increase allowance fails, approve the contract to spend the tokens
dai.approve(contract, 10_000_000 * 10**18, {'from': dev})
usdc.approve(contract, 10_000_000 * 10**6, {'from': dev})

contract.increaseLiquidityCurrentRange(contract.tokenId(), 10000 * 10**18, 10000 * 10**6, {'from': dev})
contract.getLiquidity(contract.tokenId())
contract.deposits(contract.tokenId())

contract.getLiquidty(contract.tokenId())/10**18
contract.decreaseLiquidity(60930197197252827, contract.tokenId(), {'from': dev})
